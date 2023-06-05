#!/usr/bin/python3
'''
Program that execute an integers addition
Recives two numbers and give the result only in int format
if you only receive a number, default add this with 98
'''

def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("b must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer")
    
    return int(a) + int(b)

