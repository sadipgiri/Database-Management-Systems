#!/usr/bin/env python3
"""
	example4.py - Python3 program
	Author: Sadip Giri (sadipgiri@bennington.edu)
	Created: 10/14/2017
"""

import psycopg2
import psycopg2.extras

class Review(object):

	def __init__(self, review_dict=None):
		if review_dict is None:
			raise ValueError("No business details provided")

		self.id = review_dict['id']
		self.stars = review_dict['stars']
		self.date = review_dict['date']
		self.text = review_dict['text']
		self.useful = review_dict['useful']
		self.funny = review_dict['funny']
		self.cool = review_dict['cool']
		self.business_id = review_dict['business_id']
		self.user_id = review_dict['user_id']

	def __str__(self):
		return "ID: {0}, Stars: {1}, Date: {2}, Text: {3}, Useful: {4}, Funny: {5}, Cool: {6}, Business_id: {7}, User_id: {8}".format(
		self.id, self.stars, self.date, self.text, self.useful, self.funny, self.cool, self.business_id, self.user_id)

def get_business_review(business_name=None):
	try:
		conn = psycopg2.connect("dbname='yelp_db' user='sadipgiri'")
		cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
		cur.execute("""SELECT * FROM review r INNER JOIN business b ON b.id = r.business_id WHERE r.text IS NOT NULL AND b.name = '{0}'""".format(business_name))
		# Just Curious Why this does not work : SELECT r.text FROM..... instead of SELECT * FROM ....
		# But I know we'd get the text only by doing myreview.text (since its a dictionary)
		review = cur.fetchone()
		my_review = Review (review)
		return my_review

	except Exception as e:
		print("Unable to connect to database: {0}".format(e))

if __name__ == '__main__':
	my_review = get_business_review('Pio Pio')
	print(my_review.text)	# This way we'd get the text only...
	#print("Business name: {0}".format(business_name))	// if I want to get the text of which business it was
	# what if my_review doesnot have text field