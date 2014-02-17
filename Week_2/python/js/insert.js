use school
var types = ['exam','homework','quiz']
for(student_id = 0; student_id < 100; student_id++)
{
	for (var i = 0; i < 3; i++) 
	{
		
		db.scores.insert( { 
			'student_id' : student_id, 
			'type', types[i], 
			'score': (Math.random() * 100)
		})
	}
}