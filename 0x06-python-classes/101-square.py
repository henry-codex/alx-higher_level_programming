#!/usr/bin/python3
"""
Square module.

This module contains a class that defines a square and its size and its
position on the screen, checking if the given values are right, and a setter
and getter methods to set or get them. A __str__ method is here to handle the
use of the builtin print function. There's also an area method that returns
the area of the square, another one that handles the print of the square.
"""


class Square:
    """
    Defines a square.

    Attributes:
        size (int): The size of one edge of the square.
        position (tuple): The coordinates of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object with the given size and position.

        Args:
            size (int): The size of one edge of the square.
            position (tuple): The coordinates of the square.

        Raises:
            ValueError: If size is less than 0.
            TypeError: If size is not an integer or position is not a tuple of 2 integers.
        """
        self.size = size
        self.position = position

    def __str__(self):
        """
        Returns a string representation of the Square object.

        Returns:
            str: The string representation of the square.

        Raises:
            ValueError: If size is less than 0.
        """
        square_str = ""

        if self.size > 0:
            for y in range(self.position[1]):
                square_str += '\n'
            for x in range(self.size):
                square_str += ' ' * self.position[0]
                square_str += '#' * self.size + '\n'

        return square_str[:-1]

    @property
    def size(self):
        """
        Getter and setter for the size of the square.

        Returns:
            int: The size of one edge of the square.

        Raises:
            ValueError: If size is less than 0.
            TypeError: If size is not an integer.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """
        Getter and setter for the position of the square.

        Returns:
            tuple: The coordinates of the square.

        Raises:
            TypeError: If position is not a tuple of 2 integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2 and \
                isinstance(value[0], int) and isinstance(value[1], int):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 integers")

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """
        Prints the square with the '#' character on stdout.
        """
        if self.size > 0:
            for y in range(self.position[1]):
                print()
            for x in range(self.size):
                print(' ' * self.position[0], end='')
                print('#' * self.size)
        else:
            print()

