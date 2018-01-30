#!/usr/bin/env python3
"""
    example6.py - Python3 program
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Date: 10/24/2017
"""
import web
        
urls = (
    '/businesses_by_city', 'businesses_by_city'
)

app = web.application(urls, globals())

render = web.template.render('templates/')
#render_form = web.template.render('static/')

db = web.database(dbn='postgres', user='sadipgiri', db='yelp_db')

class businesses_by_city:
	"""docstring for business_by_city"""
	def POST(self):
		state = web.input().state
		businesses = db.select('business', where="state='{0}'".format(state))
		return render.business(businesses)

	def GET(self):
		states = db.query("SELECT DISTINCT state FROM business")
		return render.search(states)

if __name__ == "__main__":
    app.run()
        



