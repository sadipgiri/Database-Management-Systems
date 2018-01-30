#!/usr/bin/env python3
"""
    example2.py - Example queries using psycopg2
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Created: 10/14/2017
"""

import psycopg2
import psycopg2.extras


class User(object):
    """
    Model a Yelp user as a class.
    """
    def __init__(self, user_dict=None):
        """
        Create an instance of a Yelp user.
        :param user_dict: The dictionary of fields used to create the user.
        :return: User instance.
        """
        if user_dict is None:
            raise ValueError("No user details provided.")

        self.id = user_dict['id']
        self.name = user_dict['name']
        self.review_count = user_dict['review_count']
        self.yelping_since = user_dict['yelping_since']
        self.useful = user_dict['useful']
        self.funny = user_dict['funny']
        self.cool = user_dict['cool']
        self.fans = user_dict['fans']
        self.average_stars = user_dict['average_stars']

    def __str__(self):
        """
        Get back a printable string representation of User.
        :return: String representation of all fields of User.
        """
        return "Name: {0}, ID: {1}, Review Count: {2}, Yelping Since: {3}, Useful: {4}, Funny: {5}, Cool: {6}, Fans {7}, Average Stars: {8}".format(
                self.name, self.id, self.review_count, self.yelping_since, self.useful, self.funny, self.cool, self.fans, self.average_stars)


def get_user_details(name=""):
    """
    Return user details for a given user name.
    :param name: The name of the user to retrieve details for
    :return: A User object, or None if nothing is found.
    """
    try:
        # connect to the database
        conn = psycopg2.connect("dbname='yelp_db' user='sadipgiri'")

        # we're gonna use a fancy cursor that gives us back a dictionary for each row!
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        # pull out the user given the name we have - we use the (name,) tuple combined with
        # the %s token in our query string such that name gets put in the place of %s
        cur.execute("""SELECT * FROM "user" WHERE name=%s""", (name,))

        # there should only be one result for this query, but either way we only want one row back
        user = cur.fetchone()

        # make a User object and return it
        my_user = User(user)
        return my_user
    except Exception as e:
        print("Unable to connect to database: {0}".format(e))


if __name__ == '__main__':
    my_user = get_user_details('andrew')
    print(my_user)
    print("User name: {0}".format(my_user.name))
