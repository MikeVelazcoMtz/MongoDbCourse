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
	bottle.response.set_cookie("fruit",fruit) #setting a cookie
	bottle.redirect("show_fruit")

@bottle.route('/show_fruit')
def show_fruit():
	fruit = bottle.request.get_cookie("fruit") #Getting a cookie
	return bottle.template("fruit_selection.tpl", fruit = fruit)

bottle.debug(True)
bottle.run(host='localhost', port=8080)