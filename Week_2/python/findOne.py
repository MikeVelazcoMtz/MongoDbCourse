from pymongo import MongoClient
import sys

connection = MongoClient()

db = connection.students
scores = db.grades

def find():
	print "find, reporting for duty"
	query = { 'type' : "exam"}
	try:
		doc = scores.find( query ).limit(10)
	except:
		print "Error Inesperado: ", sys.exc_info()[0]
	
	for data in doc:
		print data






def find_one():
	print "find_one, reporting for duty"
	query = { 'type' :"exam"}
	try:
		doc = scores.find_one( query )
	except:
		print "Error inesperado : ", sys.exc_info()[0]
	print doc

find()

find_one()
