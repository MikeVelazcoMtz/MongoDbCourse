import pymongo

connection = pymongo.MongoClient()

db = connection.students

cur = db.grades

data = cur.find({'type' : 'homework'}).sort([('student_id', 1),('score', 1)])
i = 1
for d in data:
	print d
	if (i%2) == 0:
		print str( i ) + " Es non : " + str(d['_id'])
		db.grades.remove({'_id' : d['_id']})
	i+=1
print "Voila" , str(db.grades.count())