#!/usr/bin/env python3
"""
	problem4.py - Python3 program
	Author: Sadip Giri (sadipgiri@bennington.edu)
	Created: 10/14/2017
"""

import psycopg2
import psycopg2.extras

def insert_into_catalog(filename):

	try:
		connection = psycopg2.connect("dbname = 'catalog_db' user = 'sadipgiri'")
		cur = connection.cursor()
		with open(filename) as my_file:
			cur.copy_from(my_file, 'catalog', columns=('bib_utility_number', 'title', 'material_type', 'record_number', 'year_to_date_circ', 'last_year_to_date_circ', 'total_checkouts', 'total_renewals'), sep=",")
			#cur.copy_expert("""COPY catalog FROM STDIN DELIMITER ',' CSV""", my_file)	# Previous
			connection.commit()
			connection.close()
	except Exception as e:
		print("Unable to connect to database: {0}". format(e))

# cheking if inserted data was there:
def check():
	count_row = 0
	connection = psycopg2.connect("dbname = 'catalog_db' user = 'sadipgiri'")
	cur = connection.cursor() # don't need to convet it into dictionary since we are making a csv file
	cur.execute("""SELECT * FROM catalog""")
	total_rows = cur.fetchall()
	for row in total_rows:
		print(row)
		count_row = count_row + 1
	print("Total number of rows: {0}".format(count_row))


# this is kind of tricky so for now I just used count_row above to get the number of rows in database

def row_count():
	try: 
		connection = psycopg2.connect("dbname = 'catalog_db' user = 'sadipgiri'")
    	cur = connection.cursor() # don't need to convert it into dictionary
    	cur.execute("""SELECT COUNT(*) FROM catalog;""", [t])
		total_rows = cur.fetchall()
		return len(total_rows)
	except Exception as e:
		print("Unable to connect to database: {0}".format(e))

#insert_into_catalog('catalog_dump.txt')

# This allows us to match all rows of catalog table and compare with file
# check()
print(row_count())

# Roadblocks: inserting each line into catalog table was very hard just by looping through each row and adding values to individual attribute
#		But figured out by using helpful .copy_from() command
