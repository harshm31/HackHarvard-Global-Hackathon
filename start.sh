export SERVER_PORT=$1
forever stopall
forever start ./app.js
