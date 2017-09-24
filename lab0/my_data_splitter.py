#!/usr/bin/env python3
"""
	my_data_splitter.py - Python3 program
	Author: Sadip Giri (sadipgiri@bennington.edu)
	Created: 09/11/2017
"""

# Cleaning TSV file (here: CatalogDump file) and dumping it into second file

# create an empty file
new_clean_file = open("clean_CatalogDump.txt", "w")

with open("CatalogDump.txt", errors="ignore") as my_file:
	for i in my_file:
		line = i.split("\t")	
		values = line[0:8]	# just extracting the columns/fields ignoring tabs
		my_line = values[0] + "," + values[1] + "," + values[2] + "," + values[3] + "," + values[4] + "," + values[5] + "," + values[6] + "," + values[7] 
		new_clean_file.write(my_line + '\n')	# finally dumped into clean file

# here: my clean file is comma separated (kind of CSV file).

