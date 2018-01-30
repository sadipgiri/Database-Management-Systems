#!/usr/bin/env python3

"""
    example1 - Python3 program to find a single record in a single collection of mongodb database using pymongo.
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Created: Nov 16, 2017
"""

from pymongo import MongoClient

def find_first_business_details():
    try:
        client = MongoClient('localhost')
        database = client.yelp_db
        business_collection = database.business
        return business_collection.find_one()
    except Exception as e:
        print("Unable to connect to database: {0}".format(e))

if __name__ == '__main__':
    business_details = find_first_business_details()
    if business_details is None:
        raise ValueError("No business details provided")
    print(business_details)

