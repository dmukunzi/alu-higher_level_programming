#!/usr/bin/python3
"""Module that defines BaseGeometry with an unimplemented area method."""


class BaseGeometry:
    """Base class for geometry shapes with an unimplemented area method."""

    def area(self):
        """Raise an Exception because area is not implemented yet."""
        raise Exception("area() is not implemented")
