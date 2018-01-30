#!/usr/bin/env python3
"""
    example1.py - First example using psycopg2.
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Created: 10/14/2017
"""

import psycopg2

try:
    conn = psycopg2.connect("dbname='yelp_db' user='sadipgiri'")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM business""")
    rows = cur.fetchall()
    for row in rows:
        print("    {0}".format(row[0]))
except Exception as e:
    print("Unable to connect to database: {0}".format(e))

