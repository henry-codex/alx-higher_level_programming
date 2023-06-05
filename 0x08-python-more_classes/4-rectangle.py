#!/usr/bin/python3
'''
Empty class Rectangle that defines a rectangle
'''


class Rectangle:
    '''
    class that will contain a description of rectangle
    '''
    side = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        side = self.__width + self.__height
        if self.__width == 0 or self.__height == 0:
            return 0
        return side + side

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        return ('#' * self.__width + '\n') * (self.__height - 1) + '#' * self.__width

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

