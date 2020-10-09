'''
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

'''


def find_it(seq):
    for el in seq:
        if seq.count(el)%2 !=0:
            return el