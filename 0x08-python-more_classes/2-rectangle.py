#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialise new square
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """Get method to retrieve waidth"""
        return (self._width)

    @width.setter
    def width(self, value):
        """Setter to set value of width with exceptions"""
        if not isinstance(value, int):
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Returns area of rectangle"""
        return (self._width * self._height)

    def perimeter(self):
        """Returns rectangle perimeter"""
        if self._width == 0 or self._height == 0:
            return (0)
        return 2 * (self._width + self._height)
