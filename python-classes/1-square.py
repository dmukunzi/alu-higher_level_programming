#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute."""


class Square:
    """Class that defines a square by its private size attribute."""

    def __init__(self, size):
        """Initialize a new square with the given size, unchecked."""
        self.__size = size
