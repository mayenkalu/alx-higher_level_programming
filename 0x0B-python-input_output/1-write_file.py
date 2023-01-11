#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text="")
    """Write a string to a UTF-8text file.
    Args:
        filename(str): The name of the file to write.
        text(str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        count = f.write(text)
    return count
