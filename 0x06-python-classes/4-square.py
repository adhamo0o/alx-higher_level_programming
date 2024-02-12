#!/usr/bin/python3
"""This module defines a class to represent a square."""


class Square:
    """Represents a square with a given size.
    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initializes the square with the given size.
        Args:
            size (int, optional): The initial size of the square. Defaults to 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be non-negative")
        self.__size = size

    def size(self):
        """Returns the current size of the square.
        Returns:
            int: The size of the square.
        """
        return self.__size

    def set_size(self, value):
        """Sets the size of the square.
        Args:
            value (int): The new size of the square.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be non-negative")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
