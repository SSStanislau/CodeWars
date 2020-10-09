'''
Define a regular expression which tests if a given string representing a binary number is divisible by 5.
'''


PATTERN = r'^(0|1(10)*(0|11)(01*01|01*00(10)*(0|11))*1)+$'