export SERVER_PORT=$1
forever start ~/server/code/app.js
python3 ~/server/code/flaskapp.py
