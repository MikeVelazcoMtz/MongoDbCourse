import pymongo, sys
connection = MongoClient()

db = connection.school
scores = db.scores

def find_one():
	print "Reporting for duty"
	query = { type :"Exam"}
	try:
		doc = scores.find._one( query )
	except:
		print "Error inesperado : ", sys.exc_info()[0]
	print doc

find_one()
