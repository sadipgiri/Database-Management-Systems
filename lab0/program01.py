#!/usr/bin/env python3
"""
	program01.py - Python3 Example program.
	Author: Sadip Giri (sadipgiri@bennington.edu)
	Created: 9/11/2017
"""

print('Hello, world!')

# defining functions in Python
def my_funstion(num):
	num = num + 2
	return num

print(my_funstion(2))

# this is list in Python which is the sequence of values
l = [1,1,2,3,4,4,4]

print(l)

# this is how you slice the list
# and also len() function is use to get the length of the list
print(l[3:len(l)])

# iterating over the list is quite simple too
sum = 0
for i in l:
	sum += i
print(sum)

# this is how we define Dictionaries in Python
book = dict('title': 'The Goldfinch', 'author': 'DonnaTartt', 'checkout_count': 4982)

print(book['title'])

print("sadip" + "giri" + str(10)) # Concatenation in Python 



	



