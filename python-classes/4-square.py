#!/usr/bin/python3
"""Module that defines a Square class with a size getter and setter."""


class Square:
    """Class that defines a square with a validated private size."""

    def __init__(self, size=0):
        """Initialize a square by setting its size through the setter."""
        self.size = size

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square after validating type and value."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
