#!/usr/bin/python3
"""Module that defines a Square class with a size and an area method."""


class Square:
    """Class that defines a square by its validated private size."""

    def __init__(self, size=0):
        """Initialize a square, checking size is an int and not negative."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
