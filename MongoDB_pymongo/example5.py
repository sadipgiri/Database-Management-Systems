#!/usr/bin/env python3

"""
    example5.py - Python3 program to get length of reviews which were added from review collection before
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Created: Nov. 24, 2017
"""

from pymongo import MongoClient

def get_reviews_len(business_id):
    try:
        client = MongoClient('localhost')
        database = client.yelp_db
        businesses = database.business
        #reviews = businesses.find(business_id, {'reviews': 1, '_id': 0})
        return len(list(businesses.find(business_id, {'reviews': 1, '_id': 0}))[0]['reviews'][0])
    except Exception as e:
        print("Unable to connect to database: {0}".format(e))

if __name__ == '__main__':
    business_id = {'business_id': "mr4FiPaXTWlJ3qGzp4-7Yg"}
    print (get_reviews_len(business_id))
    
"""
    Roadblock: Was to get the number of reviews added to business collection so that I'd check if reviews were added or not!!
        Fixed It!!
            Using: len(list(reviews)[0]['reviews'][0])
                Here: at first: converted to list() python3 type since it was not recognizing the object type
                      then: took out the values of reviews by un-listing (_list_[0]) and getting the values of 'reviews' key (_dict_['reviews']) 
                      finally: I was able to use len() command to get the number of reviews of that business
"""