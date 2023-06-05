#!/usr/bin/python3
"""
Function that prints the complete name.
"""

def say_my_name(first_name, last_name=""):
    """
    Print the complete name.

    :param first_name: The first name as a string.
    :param last_name: The last name as a string (default: "").
    :raises TypeError: If either `first_name` or `last_name` is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

