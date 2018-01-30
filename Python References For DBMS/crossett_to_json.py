#!usr/bin/env Python3
"""
	crossett_to_json.py - Python3 program
	Author: Sadip Giri (sadipgiri@bennington.edu)
	Created: 09/12/2017
"""

# Cleaning TSV file (here: CatalogDump file) and dumping it into second file

import json

# create an empty file
new_clean_file = open("clean_CatalogDump_in_json.txt", "w")

with open("CatalogDump.txt", errors="ignore") as my_file:
	for i in my_file:
		line = i.split("\t")	
		values = line[0:9]	# just extracting the columns/fields ignoring tabs
		vaues_in_json = json.dumps(values)
		new_clean_file.write(values_in_json)	# finally dumped into clean file




