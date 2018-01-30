#!/usr/bin/env python3
"""
    problem3.py - Python3 program
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


def add_business(given_business):
	try:
		given_business = Business(given_business)	# needed to convert given_business into Business type (instance)
		conn = psycopg2.connect("dbname='yelp_db' user='sadipgiri'")
		cur = conn.cursor()
		cur.execute("""INSERT INTO business(id, name, neighborhood, address, city, state, postal_code, latitude, longitude, stars, review_count, is_open) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",(given_business.id, given_business.name, given_business.neighborhood, given_business.address, given_business.city, given_business.state, given_business.postal_code, given_business.latitude, given_business.longitude, given_business.stars, given_business.review_count, given_business.is_open, ))
		conn.commit()
	
	except Exception as e:
		print("Unable to connect to database: {0}".format(e))

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
	adding_business = {'id': '6Mefjghkdkndfk', 'name': 'Sadip_Giri', 'neighborhood': 'fddjkhk', 'address': 'One COlelge Drive', 'city': 'Bennignton', 'state': 'VT', 'postal_code': '05201', 'latitude': 42, 'longitude': 3243, 'stars': 3, 'review_count': 10, 'is_open': 0}
	add_business(adding_business)

	my_business = get_business_details('Sadip_Giri')
	print(my_business)

# Notes: Roadblocks: had trouble inserting into but figured by making an instance and also using .format()
