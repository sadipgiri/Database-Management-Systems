#!/usr/bin/env python3
"""
	data_to_list2.py - Python3 program. 
	Author: Sadip Giri (sadipgiri@bennington.edu)
	Created: 09/12/2017
"""

lst = []

with open("CatalogDump.txt", errors="ignore") as my_file:
	for line in my_file:
		lst.append(line)

print(lst[0])