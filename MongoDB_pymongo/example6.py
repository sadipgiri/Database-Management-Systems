#!/usr/bin/env python3

"""
    example6.py - Python3 program for implementing progressbar in the terminal. This is me just trying to implement!
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Created: Nov. 25, 2017
"""

import progressbar

def sum_it(give_the_range):
    s = 0
    bar = progressbar.ProgressBar()
    for i in bar(range(give_the_range)):
        s = s + i
    return s

if __name__ == '__main__':
    r = 10000000
    print(sum_it(r))

