#!/usr/bin/python3
'''
function that adds a new attribute to an object
'''


def add_attribute(obj, name, value):
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError('can \'t add new attribute')
