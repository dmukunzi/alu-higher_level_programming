#!/usr/bin/python3
"""Module that defines MyList, a list subclass with a sorted print."""


class MyList(list):
    """List subclass that can print its elements in ascending order."""

    def print_sorted(self):
        """Print the list sorted in ascending order without modifying it."""
        print(sorted(self))
