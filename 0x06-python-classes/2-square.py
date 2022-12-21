#!/usr/bin/python3
"""This is a square module.

This module contains a class that defines a square
initialise its size and verify that its size is an integer
and it is greater than or equal to 0.

"""
class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Sets the size attribute of the square object,

        Checks that the size is an integer

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        """Checks that the size is greater than or equal to 0.

        """
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
