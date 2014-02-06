#	Getting MongoDB Driver and Bottle Framework
import bottle
from pymongo import MongoClient

@bottle.route("/")
def index():
	#Getting The Connection to the MongoDB Daemon
	host = "localhost"
	port = 27017
	connection = MongoClient(host, port)

	#Selecting the DB
	db = connection.test

	#Selecting the Collection
	name = db.names

	#Getting the Data
	selectOne = name.find_one()

	return "<h1> Hello, %s !</h1>" % selectOne['name'] 

bottle.run(host = 'localhost', port = 8000)