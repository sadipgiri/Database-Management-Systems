#!/usr/bin/env python3
"""
	my_data_splitter.py - Python3 program
	Author: Sadip Giri (sadipgiri@bennington.edu)
	Created: 09/11/2017
"""

import pandas as pd

def convert_to_csv(fileName):
	# create an empty file
	new_clean_file = open("clean_CatalogDump.txt", "w")

	with open(fileName) as my_file:
		for i in my_file:
			line = i.split("\t")	
			values = line[0:8]	# just extracting the columns/fields ignoring tabs
			my_line = values[0] + "," + values[1] + "," + values[2] + "," + values[3] + "," + values[4] + "," + values[5] + "," + values[6] + "," + values[7] 
			new_clean_file.write(my_line + '\n')	# finally dumped into clean file
	
	return new_clean_file	

'''def showFieldsType(fileName):
	my_file = pd.read_csv(convert_to_csv("CatalogDump.txt"))
	print(my_file.dtypes)
'''
# did it!
convert_to_csv("CatalogDump.txt")

# Then in terminal: I did these steps:
# import pandas as pd 	# importing this pandas module
# f = pd.read_csv("clean_CatalogDump.txt")	# reading the file as CSV file
# f.dtypes 	# it shows all the types of the fields

# Error: when I wanted to change year-to-date circ field to integer
# ValueError: invalid literal for int() with base 10: 'b1000158x'



# Deleted first row of the clean_CatalogDump file so that it will be easier to copy in PSQL
'''
def deleteFirstRow(fileName):
	file = pd.read_csv("clean_CatalogDump.txt")
	file = file[1:]
	return file
'''

# NOOO
# just ignore header in psql 
# mydb=# \COPY library_catalog FROM 'clean_CatalogDump.txt' CSV HEADER DELIMITER ',';


# my myself super user
# sudo -u postgres psql
# then it will ask for password
# psql mydb
# CREAT a table
# then copy as given above



