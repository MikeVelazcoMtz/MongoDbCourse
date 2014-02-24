from pymongo import MongoClient
import sys

connection = MongoClient('localhost',27017)

db = connection.students
scores = db.grades

def find():
	print "find, reporting for duty"
	query = {}
	#selector = { 'media.oembed.url' : 1, '_id' : 0}
	try:
		doc = scores.find( query ).sort('student_id', 1).skip(4).limit(1) #Doesn't accepts pymongo.ASCENDING 
		#doc = scores.find(query).sort([('student_id', 1),('score',-1)]) Multiple sorting detected!!
	except:
		print "Error Inesperado: ", sys.exc_info()[0]
	else:
		for data in doc:
			print data

find()
