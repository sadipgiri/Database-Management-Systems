#!/usr/bin/env python3

my_file = open("CatalogDump.txt")

print(my_file.seek(1)) # helps moving within the file
print(my_file.tell()) # tells us where we are in the file

my_file.close()