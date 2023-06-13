#!/usr/bin/python3
'''
Write a function that returns the number of lines of a text file
'''


def number_of_lines(filename=""):
    '''function that reads a text file (UTF8)'''
    with open(filename, encoding='utf-8') as file:
        c = 0
        for line in file:
            c += 1
        return c
