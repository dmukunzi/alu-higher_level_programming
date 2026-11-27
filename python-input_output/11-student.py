#!/usr/bin/python3
"""Module that defines a Student class that can be saved and reloaded."""


class Student:
    """Student defined by a first name, a last name and an age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with first name, last name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary description of the Student instance.

        If attrs is a list of strings, only the attributes whose names
        are in attrs are retrieved; otherwise all attributes are retrieved.
        """
        if (isinstance(attrs, list) and
                all(isinstance(a, str) for a in attrs)):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
