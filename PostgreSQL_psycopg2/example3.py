#!/usr/bin/env python3
"""
    example3.py - Python3 program
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Created: 10/14/2017
"""

import psycopg2
import psycopg2.extras

class Business(object):

    def __init__(self, business_dict=None):
        if business_dict is None:
            raise ValueError("No business details provided")
        self.id = business_dict['id']
        self.name = business_dict['name']
        self.neighborhood = business_dict['neighborhood']
        self.address = business_dict['address']
        self.city = business_dict['city']
        self.state = business_dict['state']
        self.postal_code = business_dict['postal_code']
        self.latitude = business_dict['latitude']
        self.longitude = business_dict['longitude']
        self.stars = business_dict['stars']
        self.review_count = business_dict['review_count']
        self.is_open = business_dict['is_open']

    def __str__(self):
        return "Name: {0}, ID: {1}, Neighborhood: {2}, Address: {3}, City: {4}, State: {5}, Postal Code: {6}, Latitude: {7}, Longitude: {8}, Stars: {9}, Review Count: {10}, Is Open: {11}".format(
        self.name, self.id, self.neighborhood, self.address, self.city, self.state, self.postal_code, self.latitude, self.longitude, self.stars, self.review_count, self.is_open)

def get_business_details(name=""):
	try:
		conn = psycopg2.connect("dbname='yelp_db' user='sadipgiri'")
		cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
		cur.execute("""SELECT * FROM business WHERE name = '{0}'""".format(name))
		business = cur.fetchone()
		my_business = Business (business)
		return my_business
	except Exception as e:
		print("Unable to connect to database: {0}".format(e))

if __name__ == '__main__':
	my_business = get_business_details('Primal Brewery')	# "" quotation marks needed around '' for string
	print(my_business)
	print("Business name: {0}".format(my_business.name))
