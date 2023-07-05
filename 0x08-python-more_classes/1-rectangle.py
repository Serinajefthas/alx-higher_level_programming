#!/usr/bin/python3
"""Class defining Rectangle object"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialise new square
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get method to retrieve width"""
        return (self._width)

    @width.setter
    def width(self, value):
        """Setter to set value of width with exceptions"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Get method to retrieve height"""
        return (self._height)

    @height.setter
    def height(self, value):
        """Setter to set value of height with exceptions"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        self._height = value
