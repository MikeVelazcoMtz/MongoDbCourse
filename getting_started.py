from pymongo import MongoClient

#Enviroment Variables
host = "localhost"
port = 27017 # Default MongoDB Port

# Set Up the Connection

connection = MongoClient(host, port)

db = connection.test # MySQL USE command Like ( Selecting  the DB)

names = db.names # Selecting (or creating)  the 'names'  collection

select_one = names.find_one() # Selecting One record from names

item = select_one['name'] # selecting from the "Result"

print item
