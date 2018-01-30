#!/usr/bin/env python3
"""
	data_copy2.py - Python3 program.
	Author: Sadip Giri (sadipgiri@bennington.edu)
	Created: 9/12/2017
"""

lst = []

with open("CatalogDump.txt", errors="ignore") as my_file:
	for i in my_file:
		lst.append(i)

new_file = open("new_CatalogDump.txt", "w")

for i in lst:
	new_file.write(i)

new_file.close()

