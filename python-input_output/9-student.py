#!/usr/bin/python3
"""Module that defines a Student class with a JSON description method."""


class Student:
    """Student defined by a first name, a last name and an age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with first name, last name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary description of the Student instance."""
        return self.__dict__.copy()
