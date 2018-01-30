#!/usr/bin/env python3

"""
	example1.py - Python3 program
	Author: Sadip Giri (sadipgiri@bennington.edu)
	Created: 10/22/2017
"""

import web

urls = (
	'/tacos', 'tacos',
	'/(.*)', 'hello'
)

app = web.application(urls, globals())

class hello:
	"""docstring for hello"""
	def GET(self, name):
		if not name:
			name = 'World'
		return 'Hello, ' + name + '!'

class tacos:
	"""docstring for tacos"""
	# def GET(self):
	# 	return 'Yum, yum, tacos!'
	def GET(self):
		html_scipt = """<html>
		<head>
		<title>
		Taco Image
		</title>
		</head>
		<body>
		<img src = "/static/100.png">
		<strong> 
		Yum, yum, tacos!
		</strong>
		</body>
		</html>"""
		return html_scipt 
		

if __name__ == '__main__':
	app.run()

