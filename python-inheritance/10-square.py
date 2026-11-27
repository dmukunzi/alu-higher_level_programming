#!/usr/bin/python3
"""Module that defines a Square class based on Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square with a validated private size, built on Rectangle."""

    def __init__(self, size):
        """Initialize the square after validating its size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
