# project2-oo89 Oscar Ojeda  

CS490 

O2TicTacToe

Heroku link: https://o2tictactoe.herokuapp.com/

## Requirements
1. `npm install`
2. `pip install -r requirements.txt`
3. `pip install flask`
4. `npm install -g heroku`
5. `pip install flask-socketio`
6. Run `pip install flask-cors`
7. cd into project directory. Run `npm install socket.io-client --save`


## Setup
1. Run `echo "DANGEROUSLY_DISABLE_HOST_CHECK=true" > .env.development.local` in the project directory
2. Make sure to clone the milestone1 branch for project2 first part. 
3. Push milestone1 branch to heroku
4. Have heroku automatically updated from milestone1 brach from GitHub 

## Run Application
1. Run command in terminal (in your project directory): `python app.py`
2. Run command in another terminal, `cd` into the project directory, and run `npm run start`
3. Preview web page in browser '/'

## Deploy to Heroku
*Project 2*
1. Create a Heroku app: `heroku create --buildpack heroku/python`
2. Add nodejs buildpack: `heroku buildpacks:add --index 1 heroku/nodejs`
3. Push to Heroku: `git push heroku milestone1`


## Technical issues
1. The first technical issue that I had was with Cloud9 virtual disk runing out of space.
I fixed this by going to AWS console from vocareum, instead of clicking Cloud9 click All
services -> EC2. Then under resources click Volumes, right click the column size on the row
that says 10GiB, then click modify volume. I put there 20GiB, then click modify and confirm. 
2. The app on Heroku at the first time didn't work, it was because the requirements.
To solve this I added everything heroku need in the requirements document in order to run. 
3. 

## Problems
1. The first problem that clearly I had for this project was the time. 
After I had the react-started code I implement the components to have the Board
and Squares but as I din't have any experience with react, JavaScript, and Socketio 
was really hard for me to get the clients updated. If I had had more time I would 
have studied the subject more and that could have helped me with this project. 
Also I think the demos and examples for this project they were very simple nothing
to do with the actual project.
2. 