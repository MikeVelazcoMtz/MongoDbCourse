import bottle

@bottle.route("/")
def home_page():
	mythings = ["apple","pear", "Lemon", "pineapple"]
	return bottle.template("hello_world",username = "Andrew", things= mythings, )

@bottle.post("/favorite_fruit")
def favorite_fruit():
	fruit =  bottle.request.forms.get('fruit') #getting the data from the form
	if (fruit == None or fruit == ""):
		fruit = "Fruit Not Selected :("
	return bottle.template("fruit_selection.tpl", fruit = fruit)

bottle.debug(True)
bottle.run(host='localhost', port=8080)