/**
 * This requires a MongoDB server to be up and running at the path as specified by the connection string
 * Link to documentation for connection string - https://docs.mongodb.com/manual/reference/connection-string/
 * If the mongodb server is running on the default port on localhost then the given connection string should work fine.
 * **/
var express = require('express')
var mongo = require('mongojs')
var app = express()

connection_string = 'climatedb'
var db = mongo(connection_string, ['climate'])

//Port to run the web server on
const PORT = 3000
const requestValidator = function(req, res, next){
	if(req.method != 'GET'){
		res.status(405)
		res.send({'error':'This method is currently not supported by this server'})
	}else{
		if('city' in req.query && req.query['city'] != null && req.query['city'] != undefined){
			next()	
		}else{
			res.status(422)	
			res.send({'error':'Invalid parameters'})
		}	
	}	

}
app.use(requestValidator)


/** route: GET /climateData
 *  example:
 *  localhost:3000/climateData?city=agra
 * **/
app.get('/climateData', function(req, res){
	const city = req.query.city
	db.climate.find({'city':city}, function(err, docs){
		if(docs.size != 0){
			res.send(docs)	
		}else{
			res.status(204)
			res.end()
		}
	})
})

app.listen(PORT, function(){
	console.log('App is running on Port number ' + PORT)
})
