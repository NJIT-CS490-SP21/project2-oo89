# project2-oo89 Oscar Ojeda

CS490

O2TicTacToe

Heroku link: https://o2m2tictactoe.herokuapp.com/

## Requirements

1. `npm install`
2. `pip install -r requirements.txt`
3. `pip install flask`
4. `npm install -g heroku`
5. `pip install flask-socketio`
6. Run `pip install flask-cors`
7. cd into project directory. Run `npm install socket.io-client --save`
8. `pip install Flask-SQLAlchemy==2.1`
9. `pip install react`

## Setup

1. Run `echo "DANGEROUSLY_DISABLE_HOST_CHECK=true" > .env.development.local` in the project directory
2. Make sure to clone the milestone_2 branch for project2.
3. Push milestone2 branch to heroku.
4. Have heroku automatically updated from milestone_2 brach from GitHub.

5. `git checkout main`
6. `git merge milestone_1`
7. `git push origin main`
8. `git branch milestone_2`
9. `git push origin milestone_2`
10. `from flask_sqlalchemy import SQLAlchemy` -> app.py
11. `from collections import OrderedDict` -> app.py
12. It is really import to have the app.py with everything I have in order for it to work.

## Run Application

1. Run command in terminal (in your project directory): `python app.py`
2. Run command in another terminal, `cd` into the project directory, and run `npm run start`
3. Preview web page in browser '/'

## Deploy to Heroku

_Project 2_

1.  First make sure there are no heroku app in the directory.
    to check this you should run `git remote -v`. If you see a heroku app run `git remote rm heroku`.
2.  Create a Heroku app: `heroku create --buildpack heroku/python`
3.  Add nodejs buildpack: `heroku buildpacks:add --index 1 heroku/nodejs`
4.  Important to have the Procfile with `web: python app.py` or the name of your main app.
5.  Push to Heroku: `git push heroku milestone2`
6.  Also you can have heroku configure to automatically update from your GitHub milestone2 branch.
    So each time you push something to GitHub your project with automatically deploy to heroku.
7.  `heroku addons:create heroku-postgresql:hobby-dev`
8.  `heroku config` (check your env vars)
9.  export DATABASE_URL='set the URL what you got from heroku config
    you can also save it in a .env file. This information is also on heroku web page, you go to you app and then settings, Config Vars.
10. Important to update your requirements.txt with newly installed Python stuff like Flask-SQLAlchemy and psycopg2.

## Technical issues

1. The first technical issue that I had was with Cloud9 virtual disk runing out of space.
   I fixed this by going to AWS console from vocareum, instead of clicking Cloud9 click All
   services -> EC2. Then under resources click Volumes, right click the column size on the row
   that says 10GiB, then click modify volume. I put there 20GiB, then click modify and confirm.
2. The app on Heroku at the first time didn't work, it was because the requirements.
   To solve this I added everything heroku need in the requirements document in order to run.
3. It is super annoying each time cloud9 automatically close your work and make you login
   agian. If you have to work for long hours, as I did, this will affects a lot.
4. As this project has a lot of part one technical issue I had was with heroku database,
   most of the times I saw this error, sqlalchemy.exc.TimeoutError: This prevent the applicantion to work as it
   is supposed, I went to https://data.heroku.com/datastores to check my database and I saw that heroku only allows 20
   connections to it and it was 20/20. The temporary solution was to run agian the app.py each time this appears.
   It is important when grading this project if you have this problem that leaderboard doesn't show the user or something
   in that order it is because the connection problem with heroku databese.
5. One of the biggest technical issue I had for this project2 was trying to send a ordered dictionary in python to JavaScript
   When I got the information I needed from the database and I save in a objects list but after that I put all that info in a Dictionary
   with key username and value score in orther to easily access the information, after a lot of research I found that JavaScript doesn’t conserve
   dictionaries order, so each time I emited the information the order changed. This is really important in this project as you need to show the
   leaderboard sorted. The solution I found was to save all of this in two list and send it like that to JavaScript.

## Problems

1. The first problem that clearly I had for this project was the time.
   After I had the react-started code I implement the components to have the Board
   and Squares but as I din't have any experience with react, JavaScript, and Socketio
   was really hard for me to get the clients updated. If I had had more time I would
   have studied the subject more and that could have helped me with this project.
   Also I think the demos and examples for this project they were very simple nothing
   to do with the actual project.
2. I had a big problem trying to update all the clients. At first I was using the same
   history and I was not making copies, after long hours studying it I realized that
   I not only had to copy the history but everything that I need to use.
   It was also important to emit from the onclick of the square all the variables that were
   going to be needed later in the useEffect. After all that, the game updates correctly on the tabs.
3. I had problem while deploying the app on heroku. The best way to avoid this problem is by:
   3.1-> First make sure there are no heroku app in the directory.
   to check this you should run `git remote -v`. If you see a heroku app run `git remote rm heroku`.
   3.2 -> `heroku create --buildpack heroku/python`
   3.3 -> `heroku buildpacks:add --index 1 heroku/nodejs`
   3.4 -> `git push heroku {your_branch_name}:main`
4. Another problem I was having with the Database. All the Config vars were configured correctly but each
   time I tried to do something to the database I got an error. The main problem was that I didn't have `if __name__ == "__main__":`
   but after fixinf that I had another problem with it and I solved by creating the table manually in python command.

# External Link I used for help with all the problem and technical issues.

1. Slack post https://cs490spring21.slack.com/archives/C01N2QP4ZSS/p1614627355385400
2. Markdown https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
3. Lecture 12 demo code https://gist.github.com/naman-njit/a35970da2de84d9640fee606d2526d6f
4. Correct way to deploy app https://cs490spring21.slack.com/archives/C01N2QP4ZSS/p1614480674198200
5. Conditional rendering https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table
6. How do you update an existing DB row with SQLAlchemy https://stackoverflow.com/questions/29194926/python-flask-db-session-commit-is-not-working
7. Slack post https://cs490spring21.slack.com/archives/C01JGC4QWLE/p1614990494032600
8. Flask-SQLAlchemy documentation: http://flask-sqlalchemy.pocoo.org/2.1/
9. Too many connections error? https://www.atemon.com/blog/pgerror-fatal-too-many-connections-for-role-xxxxxxx/
