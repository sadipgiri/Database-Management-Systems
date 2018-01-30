#!/usr/bin/env python3

"""
   example2 - Python3 program to get entire list of the businesses using pymongo from mongodb
   Author: Sadip Giri (sadipgiri@bennington.edu)
   Created: Nov 16, 2017
"""

from pymongo import MongoClient

def get_entire_list_of_businesses():
    try:
        client = MongoClient('localhost')
        database = client.yelp_db
        businesses = database.business
        my_businesses = businesses.find({'city': "Scottsdale", 'state': "AZ"}, {'name': 1, '_id': 0})   # only extracting the names of the businesses according to given query
        return my_businesses   
    except Exception as e:
        print("Unable to connect to database: {0}".format(e))

# created another function to print all the businesses names
def print_all_businesses_name (businesses_list_in_dict):
    for business in businesses_list_in_dict:
        print(business['name']) # wanted names not a dictionary containing names

if __name__ == '__main__':
    businesses_from_scott_az = get_entire_list_of_businesses()
    if businesses_from_scott_az is None:
        raise ValueError("No business details provided")
    print_all_businesses_name(businesses_from_scott_az)