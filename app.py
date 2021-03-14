import os
#from collections import OrderedDict
from flask import Flask, send_from_directory, json
from flask_socketio import SocketIO
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())  # This is to load your env variables from .env

app = Flask(__name__, static_folder='./build/static')

# Point SQLAlchemy to your Heroku database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
# Gets rid of a warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# IMPORTANT: This must be AFTER creating db variable to prevent
# circular import issues

import models
db.create_all()

cors = CORS(app, resources={r"/*": {"origins": "*"}})

socketio = SocketIO(app,
                    cors_allowed_origins="*",
                    json=json,
                    manage_session=False)


@app.route('/', defaults={"filename": "index.html"})
@app.route('/<path:filename>')
def index(filename):
    return send_from_directory('./build', filename)

#break function in order to test the code without mocking 
def sortDic(usersDic):
    usersSorted = dict(
        sorted(usersDic.items(), key=lambda item: item[1], reverse=True))
    print(usersSorted)    
    return usersSorted
    
#adding to the two lists from sorted dic
def addUsersScoresToLists(usersSortDic):
    usersList = []
    scoreList = []
    for k, v in usersSortDic.items():
        usersList.append(k)
        scoreList.append(v)
    return usersList, scoreList
    
#Count profit is a funtion to know how many dolars a user have won or lost in the game. 1 game = $1   
def calculateProfit(usersList, scoreList):
    profit = {}
    for x in range(len(usersList)):
        wonGames = scoreList[x] - 100
        profit[usersList[x]] = wonGames
    return profit
    
    
# This funtion is to get users from the DB. 
def getUserDB():
    allUsers = models.Person.query.all()
    users = {}
    for person in allUsers:
        users[person.username] = person.score
    print("no sorted")
    print(users)
    usersSorted = sortDic(users)
    print("sorted")
    print(usersSorted)
    return addUsersScoresToLists(usersSorted)
    
# Add user to DB 
def addNewUserDB(userText):
    #Addding the user to the db when login with score=100
    newUser = models.Person(username=userText, score=100)
    db.session.add(newUser)
    db.session.commit()
    allUsers = models.Person.query.all()
    users = {}
    for person in allUsers:
        users[person.username] = person.score

    usersSorted = sortDic(users)
    return addUsersScoresToLists(usersSorted)
    
# Update the the winner score and also the loser
def updateWinnerLoser(winnerName, loserName):
    dbWinner = db.session.query(models.Person).get(winnerName)
    dbLoser = db.session.query(models.Person).get(loserName)
    dbWinner.score = dbWinner.score + 1
    dbLoser.score = dbLoser.score - 1
    
    db.session.commit()
    allUsers = models.Person.query.all()
    users = {}
    for person in allUsers:
        users[person.username] = person.score

    usersSorted = sortDic(users)
    return addUsersScoresToLists(usersSorted)
    
# When a client connects from this Socket connection, this function is run
@socketio.on('connect')
def on_connect():
    print('User connected!')
    usersList, scoreList = getUserDB()
    socketio.emit('user_dic', {'users': usersList, 'scores': scoreList})
    
# When a client disconnects from this Socket connection, this function is run
@socketio.on('disconnect')
def on_disconnect():
    print('User disconnected!')

# When a client emits the event 'eventData' to the server, this function is run
# 'eventData' is a custom event name that we just decided
@socketio.on('eventData')
def on_chat(data):  # data is whatever arg you pass in your emit call on client
    socketio.emit('eventData', data, broadcast=True, include_self=False)

#Jump
@socketio.on('jump')
def on_jump(data):
    socketio.emit('jump', data)

#Login information server
@socketio.on('login')
def on_board(
        data):  # data is whatever arg you pass in your emit call on client
    #users.append(data['userText'])
    print("USer Login" + str(data))
    x = models.Person.query.filter_by(username=data['userText']).first()
    print(x)
    if x is None:
        usersList, scoreList = addNewUserDB(data['userText'])
        socketio.emit('login', data, broadcast=True, include_self=False)
        socketio.emit('user_dic', {'users': usersList, 'scores': scoreList})

    else:
        usersList, scoreList = getUserDB()
        socketio.emit('login', data, broadcast=True, include_self=False)
        socketio.emit('user_dic', {'users': usersList, 'scores': scoreList})

#update winner in db and then emit it to all the clients
@socketio.on('winnerN')
def on_winner(
        data):  # data is whatever arg you pass in your emit call on client
    print(data['winner'])
    print(data['loser'])
    winnerName = data['winner']
    loserName = data['loser']
    usersList, scoreList = updateWinnerLoser(winnerName, loserName)
    print(calculateProfit(usersList,scoreList))
    socketio.emit('user_dic', {'users': usersList, 'scores': scoreList})
    #socketio.emit('winnerN',  data, broadcast=True, include_self=False)
    
# Note we need to add this line so we can import app in the python shell
if __name__ == "__main__":

    # Note that we don't call app.run anymore. We call socketio.run with app arg
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
    )
