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
			
			# Roadblock: ignore file titles (first row) not efficient to delete or count lines in file to ignore
			# so I manually deleted the file's title
			#for i in xrange(1,get_number_of_lines(my_file)):
				#row = my_file[1]

			for row in my_file:
				ls = row.split(',')
				#cur.execute("""INSERT INTO catalog(bib_utility_number, title, material_type, record_number, year_to_date_circ, last_year_to_date_circ, total_checkouts, total_renewals) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);""",(ls[0], ls[1], ls[2], ls[3], ls[4], ls[5], ls[6], ls[7], ))
				cur.execute("INSERT INTO catalog VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (ls[0], ls[1], ls[2], ls[3], ls[4], ls[5], ls[6], ls[7], ))
				connection.commit()
			cur.close()
	except Exception as e:
		print("Unable to connect to database: {0}".format(e))

# to calcualte the number of lines in given file
def get_number_of_lines(filename):
	s = 0
	with open(filename, 'r') as f:
		s = s + 1
	return s

insert_into_catalog('catalog_dump.txt')

