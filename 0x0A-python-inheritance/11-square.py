#!/usr/bin/python3
"""Defines a class Square based on BaseGeometry class

Attributes:
    size (int): size of one side of the square
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """class Square"""

    def __init__(self, size):
        """Initialise new square object
        Args:
            size (int): size of one side of square
        """
        self._size = size
        self.integer_validator("size", size)

    def area(self, size):
        """Area of the square"""
        return self._size ** 2

    def __str__(self):
        """Funtion to print width/height

        Returns:
            Return width/height
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
