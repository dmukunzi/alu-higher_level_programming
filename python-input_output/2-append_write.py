#!/usr/bin/python3
"""Module that provides a function to append a string to a text file."""


def append_write(filename="", text=""):
    """Append text to a UTF8 file, creating it if needed, return the length."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
