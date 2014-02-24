from pymongo import MongoClient
import sys

connection = MongoClient()

db = connection.students
scores = db.grades

def find():
	print "find, reporting for duty"
	query = { 'type' : "exam", 'score': { '$gt' : 50, '$lt' : 70 }  }
	try:
		doc = scores.find( query ).limit(10)
	except:
		print "Error Inesperado: ", sys.exc_info()[0]
	
	for data in doc:
		print data

find()