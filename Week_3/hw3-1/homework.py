# for d2 in d1['scores']:
# 		if d2['type'] == "homework":
# 			print "id: " + str(d1['_id']) + " type : " + d2['type'] + " score: " + str(d2['score'])
import pymongo

connection = pymongo.MongoClient()

db = connection.school

cur = db.students

#data = cur.find({'type' : 'homework'}).sort([('_id', 1),('scores.score', 1)])
bidimensional = []
i = 0
data = cur.find({},{'name' : False,'scores':{'$slice' : [2,2]}}).sort([('_id', 1),('scores.score',-1)])
for d1 in data:
	print d1
	for d2 in d1['scores']:
		if d2['type'] == 'homework':
			bidimensional.append({'_id' : d1['_id'],'type': 'homework','score' : d2['score'] })

print len(bidimensional)
elimina = []
id = None
value = None
for d in bidimensional:
	if (i%2) != 0:#	nones
		id = d['_id']
		#print "Numero par" + str(i)
		if value > d:# si el valor anterior es mayor al actual
			elimina.append(d)
		else:
			elimina.append(value)
		value = None
	else:
		value = d
	i+=1
for d in elimina:
	obj = {'type' : d['type'],'score' : d['score']}
	db.students.update({'_id' : d['_id']},{'$pull': {'scores' :obj}})