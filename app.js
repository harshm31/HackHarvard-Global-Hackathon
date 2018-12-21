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
const PORT = process.env['SERVER_PORT']
const requestValidator = function(req, res, next){
	if(req.method != 'GET'){
		res.status(405)
		res.send({'error':'This method is currently not supported by this server'})
	}else{
		next()
	}	
}
app.use(requestValidator)


const monthMapping = {'Mar': 3, 'Feb': 2, 'Aug': 8, 'Apr': 4, 'June': 6, 'Jan': 1, 'May':5, 'Nov': 11, 'July': 7, 'Dec': 12, 'Sept': 9, 'Oct': 10, 'Year':-1}


/** route: GET /climateData
 *  example:
 *  localhost:3000/climateData?city=agra
 * **/
app.get('/climateData', function(req, res){
	const city = req.query.city.toLowerCase()
	db.climate.find({'city':city}, function(err, docs){
		if( docs==undefined || docs.size == 0){
			console.log(err)
			res.status(204)
			res.end()
		}else{
			res.send(docs)	
		}
	})
})

/** route: GET /monthMapping
 *  Returns a mapping between month_name('string') and month_num('int')
 * **/
app.get('/monthMapping', function(req, res){
	res.send(monthMapping)
})



app.listen(PORT, function(){
	console.log('App is running on Port number ' + PORT)
})
