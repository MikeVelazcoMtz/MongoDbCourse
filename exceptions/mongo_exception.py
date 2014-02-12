import sys 
from pymongo import MongoClient

connection = MongoClient("localhost", 27017)

db    = connection.test
users = db.users
doc   = { 'firstName': 'Andrew', 'lastName' : 'Ericsson'}
print doc # First Console exit
print """------------
About to insert the document """

try:
	users.insert( doc ) # After the insertion, the doc variable has a _id attribute assigned 
except:
	print "insert Failed: ", sys.exc_info()[0]

print doc	
print """------------
About to insert the document Again """
# if you really want to insert twice then uncomment the line below: 
#doc   = { 'firstName': 'Andrew', 'lastName' : 'Ericsson'}


try:
	users.insert( doc )
except:
	# it will fail because it has an assigned ID and cannot be duplicity in the ID's
	print "insert Failed Again: ", sys.exc_info()[0]