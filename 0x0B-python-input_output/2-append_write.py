#!/usr/bin/python3
"""
Defines an append_write function.
"""

def append_write(filename="", text=""):
    """returns the number of characters appended to a UTF8-text file"""
    with open(filename, 'a', encoding='utf8') as f:
        return f.write(text)
