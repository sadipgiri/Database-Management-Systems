#!/usr/bin/env python3
"""
	web_data_retriever.py - Python3 program
	Author: Sadip Giri (sadipgiri@bennington.edu)
	Created: 12/09/2017
"""
import requests	

def write_into_file(web_address):
	response = requests.get(web_address)
	text = response.text
	my_file = open("newFile.txt", "w")
	for i in text:
		my_file.write(i)
	my_file.close()

write_into_file("http://cs.bennington.edu/courses/f2017/cs4311.01/data/CatalogDump.txt")