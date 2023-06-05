#!/usr/bin/python3
"""
Empty class Rectangle that defines a rectangle.
"""


class Rectangle:
    """
    Class that contains the description of a rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        :param width: The width of the rectangle (default: 0).
        :param height: The height of the rectangle (default: 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        :param value: The width value to set.
        :raises TypeError: If the value is not an integer.
        :raises ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        :param value: The height value to set.
        :raises TypeError: If the value is not an integer.
        :raises ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

