#!/usr/bin/env python3
"""
    example2.py - Python3 program
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Date: 10/23/2017
"""
import web

render = web.template.render('templates/')
        
urls = (
    '/tacos/(.*)', 'tacos', 
    '/(.*)', 'hello'
)

app = web.application(urls, globals())

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


if __name__ == "__main__":
    app.run()
        



