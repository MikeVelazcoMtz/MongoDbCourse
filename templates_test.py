import bottle

@bottle.route("/")
def home_page():
	mythings = ["apple","pear", "Lemon", "pineapple"]
	return bottle.template("hello_world",username = "Andrew", things= mythings, )

@bottle.route("/testpage")
def test_page():
	return "This is a test page"

bottle.debug(True)
bottle.run(host='localhost', port=8080)