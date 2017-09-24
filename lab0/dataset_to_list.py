#!/usr/bin/env python3
"""
	dataset_to_list.py - Python3 program
	Author: Sadip Giri (sadipgiri@bennington.edu)
	created: 9/12/2017
"""

lst = []

my_file = open("CatalogDump.txt", errors="ignore") # ignored encoding errors of the file

for i in my_file:
	lst.append(i)

my_file.close()

print(lst[0])	# printed particular line of the file to check the list contain

