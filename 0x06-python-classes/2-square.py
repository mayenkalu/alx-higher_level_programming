#!/usr/bin/python3
"""This is a square module.

This module contains a class that defines a square
initialise its size and verify that its size is an integer
and it is greater than or equal to 0.

"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Sets the size attribute of the square object.

        Args:
            size(int): the size of one side of the square.

        Raises:
            TypeError: if size is an integer.
            ValueError: if size is grater than or equal to 0.
        """
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
