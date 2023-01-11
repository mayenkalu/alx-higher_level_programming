#!/usr/bin/python3
"""
Defines a file-writing function.
"""


def write_file(filename="", text=""):
    """returns the number of characters written to a UTF-8 text file."""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
