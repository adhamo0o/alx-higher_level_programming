#!/usr/bin/python3
"""This is a class called square."""


class Square:
    """This class that defines a square."""
    def __init__(self, size=0):
        """
        Initializes the square with the given size.
        Args:
            size (int): The size of a square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
