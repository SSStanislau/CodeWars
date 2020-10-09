'''
Complete the greatestProduct method so that it'll find the greatest product of five consecutive digits in the given string of digits.

For example:

greatestProduct("123834539327238239583") // should return 3240

The input string always has more than five digits.

Adapted from Project Euler.

'''


def greatest_product(n):
    res = 0
    tmp = 1
    for i in range(len(n)-4):
        for j in n[i:i+5]:
            tmp *=int(j)
        if tmp > res:
            res = tmp
            tmp = 1
        else:
            tmp = 1
    return res
        