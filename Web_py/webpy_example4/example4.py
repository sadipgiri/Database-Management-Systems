#!/usr/bin/env python3
"""
    example4.py - Python3 program
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Date: 10/23/2017
"""
import web
        
urls = (
    '/tacos/(.*)', 'tacos',
    '/muncher', 'muncher',
    '/businesses_by_city', 'businesses_by_city',
    '/businessinfo/(.*)', 'business_info',
    '/(.*)', 'hello'
)

app = web.application(urls, globals())

render = web.template.render('templates/')
render_form = web.template.render('static/')

db = web.database(dbn='postgres', user='sadipgiri', db='yelp_db')

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

class businesses_by_city:
	"""docstring for business_by_city"""
	def POST(self):
		city = web.input().city
		businesses = db.select('business', where="city='{0}'".format(city))
		#business = db.query("select * from business where city='{0}'".format(city))
		return render.business(businesses)

	def GET(self):
		return render_form.search()

class business_info:
	"""docstring for business_info"""
	def GET(self, business_id):
		if business_id:
			business_info = db.select('business', where="id='{0}'".format(business_id))
			return render.business_info(business_info)
		else:
			return "Can't find information of the businesss as given."



if __name__ == "__main__":
    app.run()
        



