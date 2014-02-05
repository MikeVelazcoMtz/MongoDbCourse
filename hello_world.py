from bottle import route, run, template

@route("/hello/:name")
def index( name = "World" ):
	return template("<h1>Hello, {{name}} !</h1>", name = name)

run(host="localhost",port = 8000)
