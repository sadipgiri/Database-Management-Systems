#!/usr/bin/env python3
"""
    example3.py - Python3 program
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Date: 10/23/2017
"""
import web
        
urls = (
    '/tacos/(.*)', 'tacos',
    '/muncher', 'muncher',
    '/(.*)', 'hello'
)

app = web.application(urls, globals())

render = web.template.render('templates/')
render_form = web.template.render('static/')

class hello:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class tacos:
    """docstring for Tacos"""
 	#def GET(self):
	# 	return 'Yum, yum, tacos!'
	#def GET(self):
	# 	html_scipt = """<html>
	# 	<head>
	# 	<title>
	# 	Taco Image
	# 	</title>
	# 	</head>
	# 	<body>
	# 	<img src = "/static/100.png">
	# 	<strong> 
	# 	Yum, yum, tacos!
	# 	</strong>
	# 	</body>
	# 	</html>"""
	# 	return html_scipt
    def GET(self, name):
        return render.tacos(name)

class muncher:
	"""docstring for muncher"""
	def POST(self):
		my_input = web.input()
		my_input1 = my_input.input1
		return render.tacos(my_input1)

	def GET(self):
		return render_form.myform()


if __name__ == "__main__":
    app.run()
        



