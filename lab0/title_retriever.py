#!/usr/bin/env python3

# this function helps us to retrieve title of any file with its file name
def title(fileName):
	my_file = open(fileName)
	title = my_file.readline()
	my_file.close()
	return title

print(title("CatalogDump.txt"))