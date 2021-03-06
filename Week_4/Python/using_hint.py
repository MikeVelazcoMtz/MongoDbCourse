import pymongo
import sys

connection = pymongo.MongoClient()

db = connection.test
foo = db.foo

query = {'a': 40000, 'b':40000, 'c': 40000}

try:
	doc = foo.find(query).hint([('c', pymongo.ASCENDING)]).explain()
except:
	print "Unexpected error:", sys.exc_info()[0]

for key in doc:
		print str(key).rjust(20), ": ", str(doc[key])