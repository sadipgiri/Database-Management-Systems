#!/usr/bin/env python3

"""
    example4.py - Python3 program to practice adding extra field within the existing data in monogodb collection
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Created: Nov. 19, 2017
"""

from pymongo import MongoClient

def add_field(match_to_existing_field, adding_field):
    try:
        client = MongoClient('localhost')
        database = client.yelp_db
        towns_collection = database.towns
        find_existing_field = towns_collection.find_one(match_to_existing_field)
        push_new_fields = towns_collection.update(find_existing_field, {'$push': adding_field}) # this fixed my roadblock of adding extra field in mongodb collection
    except Exception as e:
        print("Unable to connect to database: {0}".format(e))

def test_field(match_to_existing_field):
    try:
        client = MongoClient('localhost')
        database = client.yelp_db
        towns_collection = database.towns
        return towns_collection.find_one(match_to_existing_field)
    except Exception as e:
        print("Unable to connect to database: {0}".format(e))

if __name__ == '__main__':
    # testing given function
    matching_field = {'name': "New York"}
    previous = test_field(matching_field)
    print(previous)
    add_field(matching_field, {'test': "added_in_test_field"})
    new = test_field(matching_field)
    print(new)
    if previous == new:
        raise ValueError("Could not push new fields to towns collection!")
    else:
        print("Pushed into towns collection")
