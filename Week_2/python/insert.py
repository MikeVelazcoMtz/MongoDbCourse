from pymongo import MongoClient
import sys

connection = MongoClient()

db = connection.school
people = db.people

def insert():
	richard = {'name' : "Richard Kreuter", 'company' : "10gen", 
		'interests' : ['horses','skydriving','fencing'] }
	andrew = {'_id':'Erlichson','name' : 'Andrew Erlichson', 'company' : '10gen',
		'interests':['running', 'cycling','photography']}
	try:
		people.insert( richard )
		people.insert( andrew )
	except:
		print "Unexpected error:", sys.exc_info()[0]
	print(andrew)
	print(richard)

insert()
