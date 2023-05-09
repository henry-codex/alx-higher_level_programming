#!/usr/bin/python3
# 8-uppercase.py
# Brennan D Baraban <375@holbertonschool.com>

def uppercase(string):
    """Print a string in uppercase."""
    for char in string:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        print(f"{char}", end="")
    print("")
