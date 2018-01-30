#!/usr/bin/env python3

"""
    example3 - Python3 program to get reviews of a business (practicing some joins in Joinless MongoDB!!)
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Created: Nov 18, 2017
"""

from pymongo import MongoClient

def get_business_details():
    try:
        client = MongoClient('localhost')
        database = client.yelp_db
        business_collection = database.business
        business_details = business_collection.find_one({'name': "Pei Wei", 'state': "AZ", 'city': "Surprise"})
        return business_details
    except Exception as e:
        print("Unable to connect to database: {0}".format(e))

def get_reviews_of_business(business_details):
    try:
        client = MongoClient('localhost')
        database = client.yelp_db
        review_collection = database.review
        reviews = review_collection.find({'business_id': "{0}".format(business_details['business_id'])})
        return reviews
    except Exception as e:
        print("Unable to connect to database: {0}".format(e))

def print_all_reviews(get_reviews_of_business):
    for review in get_reviews_of_business:
        print(review)

# Just checking as this is not efficient way of doing as I will have to query above to get 'text' field only
def print_reviews_only(get_reviews_of_business):
    for review in get_reviews_of_business:
        print(review['text'])


if __name__ == '__main__':
    # test funciton get_business_details()
    my_business = get_business_details()
    if my_business is None:
        raise ValueError("No business details provided!")
    #print(my_business)

    # test review_details:
    my_reviews = get_reviews_of_business(my_business)
    if my_reviews is None:
        raise ValueError("No reviews provided!")
    #print_all_reviews(my_reviews)

    # test review_text only part:
    print_reviews_only(my_reviews)