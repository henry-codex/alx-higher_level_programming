#!/usr/bin/python3
# 6-print_comb3.py
# Brennan D Baraban <375@holbertonschool.com>

"""Print all possible different combinations of two digits in ascending order.
    The two digits must be different - 01 and 10 are considered identical.
   """
for i in range(0, 8):
    for j in range(i + 1, 10):
        print("{:d}{:d}".format(i, j), end=', ')
print("{:d}{:d}".format(i + 1, j))
