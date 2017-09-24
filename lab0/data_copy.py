#!/usr/bin/env python3
"""
	data_copy.py - Python3 program.
	Author: Sadip Giri (sadipgiri@bennington.edu)
	Created: 9/12/2017
"""

import os

lst = []
my_file = open("CatalogDump.txt", errors="ignore")

for i in my_file:
	lst.append(i)

print(lst[1])
my_file.close()

new_file = open("new_CatalogDump.txt", "w")

for i in lst:
	new_file.write(i)

new_file.close()








