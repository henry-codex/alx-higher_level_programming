#!/usr/bin/env python3

"""
This is a program that imports the function add(a, b) from the file add_0.py
and prints the result of the addition 1 + 2 = 3.
"""

if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
