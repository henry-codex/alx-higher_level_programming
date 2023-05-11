#!/usr/bin/python3
"""
Adds up all command line arguments and prints the result
"""

if __name__ == "__main__":
    from sys import argv

    # initialize the sum
    add = 0

    # loop through all arguments after the first one and add them up
    for s in argv[1:]:
        add += int(s)

    # print the sum
    print("{:d}".format(add))

