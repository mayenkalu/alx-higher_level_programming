#!/usr/bin/python3
"""defines a text file-appending function"""


def append_write(filename="", text="")
    """return the characters of text appended to UTF-8 text file"""
    with open(filename, 'a', encoding='utf-8') as f:
        count = f.write(text)
    return count
