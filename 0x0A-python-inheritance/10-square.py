#!/usr/bin/python3
'''
Using the class rectangle
in order to create a square
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    Class square
    '''
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)
