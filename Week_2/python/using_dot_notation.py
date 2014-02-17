import pymongo, sys

connection = MongoClient('localhost', 27018)

db = connection.reddit
scores = db.stories

def find():
	print "Find reporting for the duty"

	query = { 'media.oembed.type' : 'video'}
	projection = { 'media.oembed.url': 1, '_id' : 0}

	try:
		iter = scores.find( query, projection )
	except:
		print "Error inesperado"

	sanity = 0
	for doc in iter:
		print doc
		sanity += 1
		if sanity > 10:
			break

find()
