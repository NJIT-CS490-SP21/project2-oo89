import os
from flask import Flask, send_from_directory, json, session
from flask_socketio import SocketIO
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv()) # This is to load your env variables from .env

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

socketio = SocketIO(
    app,
    cors_allowed_origins="*",
    json=json,
    manage_session=False
)
current_active_users = []

@app.route('/', defaults={"filename": "index.html"})
@app.route('/<path:filename>')
def index(filename):
    return send_from_directory('./build', filename)

# When a client connects from this Socket connection, this function is run
@socketio.on('connect')
def on_connect():
    print('User connected!')

# When a client disconnects from this Socket connection, this function is run
@socketio.on('disconnect')
def on_disconnect():
    print('User disconnected!')

# When a client emits the event 'eventData' to the server, this function is run
# 'eventData' is a custom event name that we just decided
@socketio.on('eventData')
def on_chat(data): # data is whatever arg you pass in your emit call on client
    print((data['squares']))
    print((data['i']))
    print((data['history']))
    # This emits the 'eventData' event from the server to all clients except for
    # the client that emmitted the event that triggered this function
    socketio.emit('eventData',  data, broadcast=True, include_self=False)

users = []
@socketio.on('login')
def on_board(data): # data is whatever arg you pass in your emit call on client
    users.append(data['userText'])
    print()
    #print(current_active_users)
    # This emits the 'eventData' event from the server to all clients except for
    # the client that emmitted the event that triggered this function
    socketio.emit('login',  data, broadcast=True, include_self=False)    

# Note that we don't call app.run anymore. We call socketio.run with app arg
socketio.run(
    app,
    host=os.getenv('IP', '0.0.0.0'),
    port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
)