#!/usr/bin/env python3

"""
    denormalize_user_collection.py - Python3 program to denormalize yelp_db database using pymongo in mongodb by adding username in respective review collection 
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Created: Nov 25, 2017
"""

import progressbar  # Why? to show user that program is running/progressing!!
from pymongo import MongoClient

username_found = ""
username_added = ""
bar = progressbar.ProgressBar()

"""
    Optimization techniques: - added indexes in user_id in both review and user collection and also added indexing in name attribute of user collection
        - other techniques are pretty similar to that of denormalize_yelp.py
"""

def test_phase(username_found, username_added):
    if username_added != username_found:
        raise ValueError("Oops not all username added!")

def further_denormalize_yelp_one():
    try:
        print("*** Denormalization process: Started. ***")
        client = MongoClient('localhost')
        database = client.yelp_db 
        review_collection = database.review
        user_collection = database.user
        #print("*** Test phase: Started. ***")
        user_id = {'user_id': "lsSiIjAKVl-QRxKjRErBeg"}
        username = user_collection.find_one(user_id, {'name': 1, '_id': 0})
        #username_found = username['name']
        review_collection.update(user_id, {'$set': username}) 
        #username_added = review_collection.find_one({'user_id': "{0}".format(user_id['user_id']), 'name': ""}, {'name': 1, '_id': 0})['name']  
        #test_phase(username_found, username_added)
        #print("*** Test phase: Completed. ***")
        print("*** Denormalization process: Completed. ***")
    except Exception as e:
        print("Unable to connect to database: {0}".format(e))

def further_denormalize_yelp():
    try:
        print("*** Denormalization process: Started. ***")
        client = MongoClient('localhost')
        database = client.yelp_db 
        review_collection = database.review
        user_collection = database.user
        user_ids = review_collection.find({}, {'user_id': 1, '_id': 0}) # extracting only user_id's since I am joining according to user_id in user collection only
        print("*** Test phase: Started. ***")
        for user_id in bar(user_ids):
            username = user_collection.find_one(user_id, {'name': 1, '_id': 0})
            #username_found = username['name']
            #review_collection.update(user_id, {'$push': username})
            review_collection.update(user_id, {'$set': username}) 
            #username_added = review_collection.find_one(user_id, {'name': 1, '_id': 0})['name']  
            #test_phase(username_found, username_added)
        print("*** Test phase: Completed. ***")
        print("*** Denormalization process: Completed. ***")
    except Exception as e:
        print("Unable to connect to database: {0}".format(e))

"""
    Roadblocks: Testing in my way as there might be many reviews of one user with one user_id..
        # But I checked by denormalizing one entry so!!
"""

if __name__ == '__main__':
    #further_denormalize_yelp_one()
    further_denormalize_yelp()

