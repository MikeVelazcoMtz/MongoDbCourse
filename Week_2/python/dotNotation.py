from pymongo import MongoClient
import sys

connection = MongoClient()

db = connection.reddit
scores = db.stories

def find():
	print "find, reporting for duty"
	query = { 'media.oembed.type' : 'video' }
	selector = { 'media.oembed.url' : 1, '_id' : 0}
	try:
		doc = scores.find( query, selector ).limit(10) # Applying the selector = projection
	except:
		print "Error Inesperado: ", sys.exc_info()[0]
	
	for data in doc:
		print data

find()

