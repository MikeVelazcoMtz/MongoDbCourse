from pymongo import MongoClient

conn = MongoClient()

db = conn.students

grades = db.grades

query = { 'type' : "homework"}
sort = { 'score' : 1 }
info = grades.find( query ).sort('score',1).sort('student_id',1)
score = []
student = []
i = 0
for doc in info:
	score.append(doc['score'])
	student.append(doc['student_id'])

print len(score)