#!/usr/bin/python3
"""Defines a class Square based on Rectangle class

Attributes:
    width (int): width of rectangle
    height (int): height of rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square
    Args:
        Rectangle (Rectangle): rectangle object
    """

    def __init__(self, size):
        """Initialise new square object
        Args:
            size (int): size of one side of square
        """
        self._size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Area of the square

        Returns:
            int: area of square
        """
        return self._size ** 2

    def __str__(self):
        """Funtion to print width/height of square

        Returns:
            Return width/height
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
