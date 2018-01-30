#!/usr/bin/env python3

"""
    original_denormalize_yelp.py - Python3 program to denormalize yelp_db database using pymongo in mongodb
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Created: Nov 19, 2017
"""

import progressbar
from pymongo import MongoClient

# Optimization Techniques Used:
    # Created indexing in business_id of business & review collection
    # tried to talk to MongoClient only once... as before I was talking twice (to denormalize as well as to get_reviews!!)
    # used $push: {} technique to push whole list of reviews in business rather than created list/array and appending one review by another
    # For testing too: used same MongoClient() and also added two global variables for checking purposes 

# Roadblocks: (Figured out using '$set' shown in denormalization_yelp.py)
    # getting the length of the internal array of the collection attributes though it shows the type list?
        # fixed it using example5.py 
    # pass by reference (or call-by-value issue) problem occured because it was deleting reviews as well as deleteing those from 'reviews' variable. 
        # Fixed it by changing the type of reviews by giving list() as a type to it! 

# Issue here! was that I had was using '$push' for updating the business collection by adding its respective reviews
    # Fixed it! using '$set' update: I implemented it in denormalize_yelp.py

# Global Variables for testing/checking purposes:
reviews_found = 0
reviews_added = 0
bar = progressbar.ProgressBar()

# made a different function to get the reviews of a business for testing purposes (I used it for denormalizing one entry!)
# But in denormalizing whole I'd directly reference to business & review collection from one MongoClient
def get_reviews_of_business(business_id):
    try:
        client = MongoClient('localhost')
        database = client.yelp_db
        review_collection = database.review
        reviews = review_collection.find(business_id) 
        reviews = list(reviews) # changing into reviews type since the reviews were also deleted in reviews variable (interesting problem, I guess!) [check: pass-by-value or pass-by-reference in Python3]
        review_collection.delete_many(business_id)    # this delete all the reviews with satisfying given condition
        return reviews
    except Exception as e:
        print("Unable to connect to database: {0}".format(e))        

# this is for testing which involves counting reviews extracted from review collection and added in business collection
# here roadblock: I am still having trouble to get the length of the reviews after added to business collection
    # Fixed: example5.py
def test_reviews(reviews_found, reviews_added):
    if reviews_found != reviews_added:
        raise ValueError("Oops not all reviews added!")
    print("Successfully added the reviews!")
        
# Testing: checking/implementing my algorithm in one collection of data 
def denormalize_one():
    try:
        client = MongoClient('localhost')
        database = client.yelp_db
        business_collection = database.business
        # we can get review here too !! --- check it out!! ---
            # I found that that: I didn't have to make a different function for extracting reviews from review collection
                # did it in below denormalize_yelp() function
        #business_id = {'business_id': "mr4FiPaXTWlJ3qGzp4-7Yg"}    # testing an example!!
        business_id = {"business_id" : "JB8-8TtNYX-vLqN7cz-zHA"}
        reviews = get_reviews_of_business(business_id)
        business_collection.update(business_id, {'$push': {'reviews': reviews}})
    except Exception as e:
        print("Unable to connect to database: {0}".format(e))

def denormalize_yelp():
    try:
        print("*** Denormalization process: Started. ***")
        client = MongoClient('localhost')
        database = client.yelp_db 
        business_collection = database.business
        review_collection = database.review
        businesses_ids = business_collection.find({}, {'business_id': 1, '_id': 0}) # extracting only business_id's since I am joining according to business_id in review collection only
        for business_id in bar(businesses_ids):
            reviews = review_collection.find(business_id) 
            reviews = list(reviews) # changing into reviews type since the reviews were also deleted in reviews variable (interesting problem, I guess!) [check: pass-by-value or pass-by-reference in Python3]
            review_collection.delete_many(business_id)    # this will delete all the reviews with satisfying given condition
            reviews_found = len(reviews)    # length of extracted reviews: for testing purposes
            print("Reviews Found: {0}".format(reviews_found))
            business_collection.update(business_id, {'$push': {'reviews': reviews}})   # this is how I am updating the business collection!! NOTE: 
            reviews_added = len(list(business_collection.find(business_id, {'reviews': 1, '_id': 0}))[0]['reviews'][0]) # I figured this out in example5.py (this is just for listing - unlisting - getting_values_from_dictionaries - and return len())
            print("Reviews_added: {0}".format(reviews_added))
            print("*** Test phase: Started. ***")
            test_reviews(reviews_found, reviews_added)
        print("*** Test Phase: Completed. ***")
        print("*** Denormalization process: Completed. ***")
    except Exception as e:
        print("Unable to connect to database: {0}".format(e))

if __name__ == '__main__':
    # What about showing Progress Bar in terminal?? Check this out!!
    # confused: should add review text only or whole review attributes of that business in array?
        # add whole review of that business there
    # and also: should add just user name of that individual review or other user attributes too?
        # just add user 'name' only of whose review was that?
    # But What about username: should I add it to review first and then add that review to business or get the review and serach user and it to business!!
    # should show where I did indexing or not? as I can easily do it in mongodb compass community?
        # let's do by adding indexes in mongodb compass community first and write it in comment

    # Andrew's Sample for implementing Denormalization with some testing phases: --
    """
        $ python3 denormalize_yelp.py   - this is done gave name as denormalize_yelp.py
        *** Denormalization process: Started. ***   - should just print it I guess! yes done
        > Iterating over businesses and consolidating reviews...
        10000
        20000
        30000
        ...
        150000
        > Review consolidation complete!
        *** Denormalization process: Complete. ***  - print this one also
        *** Test phase: Started. ***    - print this one too
        > Verifying all reviews have been consolidated for each business: PASSED *** Test phase: Complete. ***
    """
    # test get_review_of_business_function:
    # ok = get_reviews_of_business({"business_id" : "dwQEZBFen2GdihLLfWeexA"})
    # print(ok)
    # print(len(ok))
    # denormalize_one()
    denormalize_yelp()