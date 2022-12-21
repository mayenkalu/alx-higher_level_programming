#!/usr/bin/python3
"""This is a square module.

This module contains a class that defines a square, initialise
its size, verify that given values are integers and greater than
or equal to 0. A getter and setter method to get or set the values.
An area method that returns the area of the square, and a method that prints.

"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Sets the size attribute of the square object.
        Args:
            size(int): the size of one side of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print in stdout the size of the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
