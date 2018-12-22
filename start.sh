export SERVER_PORT=$1
forever stopall
forever start ~/server/code/app.js
python3 ~/server/code/flaskapp.py >> ./server_log.txt
