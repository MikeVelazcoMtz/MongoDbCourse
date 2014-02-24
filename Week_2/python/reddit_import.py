import json
import urllib2
from pymongo import MongoClient

#connect to mongo
connection = MongoClient()# Asignando los valores por default

#setting a reddit DB
db = connection.reddit
stories = db.stories

# getting the reddit home page
reddit_page = urllib2.urlopen("http://www.reddit.com/r/technology/.json")

#parse th json into python objects
parsed = json.loads(reddit_page.read())

# iterate trough every news item on the page
for item in parsed['data']['children']:
	#put it in mongo
	stories.insert(item['data'])
