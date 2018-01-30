#!/usr/bin/env python3

"""
    denormalize_yelp.py - Python3 program to denormalize yelp_db database using pymongo in mongodb
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Created: Nov 19, 2017
"""

"""
    Most of the things were done in original_denormalization_yelp.py including testing, deleting & checking! 
        but the issue was with reviews inserted in array within array by using $push update
        now I figured it out by simply using $set update in this program
        so pardon me for not doing testing (It was taking me way long time in other program so!!), deleting (I'd directly drop() review collection at last) & commenting things - similar to that original_denormalization_yelp.py
"""

import progressbar
from pymongo import MongoClient

bar = progressbar.ProgressBar()

def get_reviews_of_business(business_id):
    try:
        client = MongoClient('localhost')
        database = client.yelp_db
        review_collection = database.review
        reviews = review_collection.find(business_id) 
        reviews = list(reviews) 
        return reviews
    except Exception as e:
        print("Unable to connect to database: {0}".format(e))        
        
def denormalize_one():
    try:
        client = MongoClient('localhost')
        database = client.yelp_db
        business_collection = database.business
        #business_id = {'business_id': "mr4FiPaXTWlJ3qGzp4-7Yg"}    # testing an example!!
        business_id = {"business_id" : "JB8-8TtNYX-vLqN7cz-zHA"}
        reviews = get_reviews_of_business(business_id)
        business_collection.update(business_id, {'$set': {'reviews': reviews}})
    except Exception as e:
        print("Unable to connect to database: {0}".format(e))

def denormalize_yelp():
    try:
        print("*** Denormalization process: Started. ***")
        client = MongoClient('localhost')
        database = client.yelp_db 
        business_collection = database.business
        review_collection = database.review
        businesses_ids = business_collection.find({}, {'business_id': 1, '_id': 0}) 
        for business_id in bar(businesses_ids):
            reviews = review_collection.find(business_id) 
            reviews = list(reviews)
            business_collection.update(business_id, {'$set': {'reviews': reviews}})
        print("*** Denormalization process: Completed. ***")
    except Exception as e:
        print("Unable to connect to database: {0}".format(e))

if __name__ == '__main__':
    # ok = get_reviews_of_business({"business_id" : "dwQEZBFen2GdihLLfWeexA"})
    # print(ok)
    # print(len(ok))
    # denormalize_one()
    denormalize_yelp()
