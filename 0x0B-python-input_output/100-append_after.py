#!/usr/bin/python3
'''
Function that inserts a line of text to a file,
after each line containing a specific string
'''


def append_after(filename="", search_string="", new_string=""):
    '''Function to insert a line in specific string'''
    c = ''
    with open(filename) as file:
        for phr in file:
            c += phr
            if search_string in phr:
                c += new_string
    with open(filename, 'w') as f:
        f.write(c)
