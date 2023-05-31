#!/usr/bin/python3
"""Square module.
This module contains a class that defines a square and its size and its
position on the screen, checking if the given values are right, and a setter
and getter methods to set or get them. There's also an area method that returns
the area of the square, another one that handles the print of the square.
"""
class Square:
    """
    Class to find the area of a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Constructor for the Square class.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0 or position coordinates are less than 0.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        for x in position:
            if not isinstance(x, int) or x < 0:
                raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

    @property
    def size(self):
        """
        Getter for the size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter for the position attribute.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position attribute.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
            ValueError: If any coordinate in the tuple is less than 0.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        for x in value:
            if not isinstance(x, int) or x < 0:
                raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size**2

    def my_print(self):
        """
        Prints the square.
        """
        if self.__size == 0:
            print("")
        else:
            for x in range(self.__position[1]):
                print("")
            for _ in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)

