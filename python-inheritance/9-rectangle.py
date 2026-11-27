#!/usr/bin/python3
"""Module that defines a full Rectangle class based on BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle with area computation and a readable description."""

    def __init__(self, width, height):
        """Initialize the rectangle after validating width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the description as [Rectangle] <width>/<height>."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
