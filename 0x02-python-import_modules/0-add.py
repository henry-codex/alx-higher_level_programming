#!/usr/bin/env python3

"""
This is a program that imports the function add(a, b) from the file add_0.py
and prints the result of the addition 1 + 2 = 3.
"""

from add_0 import add

a = 1
b = 2
result = add(a, b)

print("{:d} + {:d} = {:d}".format(a, b, result))

