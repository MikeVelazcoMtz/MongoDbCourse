<!doctype html>
<html>
	<head>
		<title>Hello World Template</title>
	</head>
	<body>
		<h1>Hello {{username}}</h1>
		<ul>
			%for thing in things:
				<li>{{thing}}</li>
			%end
		</ul>
		<!-- Section for the fruit form.py -->
		<form action="/favorite_fruit" method="POST">
			<label for="fruit">Which is your favorite fruit?</label>
			<input type="text" id="fruit" name="fruit">
			<input type="submit" value="Submit">
		</form>
	</body>
</html>