from pymongo import MongoClient

class MongoClass:
	def __init__(self):
		self.host = '127.0.0.1'
		self.port = 27017
		self.conn = None
		self.db   = None
		self.table = None
	def connect(self):		
		try:
			self.conn = MongoClient(self.host, self.port)
		except:
			print "La has cagao, no se pudo conectar"
		else:
			print "Conexion exitosa"
	
	def setDB(self,database):
		print "use ", database
		self.db = self.conn[database]

	def setTable(self, table):
		#print "Seleccionando la tabla", table
		self.table = self.db[table]

	def find(self, query, select = False, limit = False):
		#help(self.table)
		print "### Ejecutando find ###"
		data = self.table.find( query )
		if select == False:
			print "data = db." + str(self.table.name) + ".find(" + str(query) + ")"
			data = self.table.find( query )
		else:	
			print "db." + str(self.table.name) + ".find(" + str(query) + ", " + str(select) + ")"
			data = self.table.find( query, select )

		if limit != False:
			print "data.limit(" + str(limit) + ")"
			data.limit(10)
		
		for d in data:
			print d

	def findOne(self, query):
		print "### Ejecutando findOne ###"
		data = self.table.find_one(query)
		print data				

instancia = MongoClass()
instancia.connect()
instancia.setDB('students')
instancia.setTable('grades')
query = {}
instancia.find( query, False, 10 )

instancia.findOne(query)
