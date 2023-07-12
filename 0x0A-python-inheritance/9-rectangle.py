#!/usr/bin/python3
"""Defines a class Rectangle based on BaseGeometry class

Attributes:
    width (int): width of the rectangle.
    height (int): height of the rectangle.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""

    def __init__(self, width, height):
        """Initialise new rectangle object
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self._width = width
        self._height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Returns area of rectangle"""
        return (self._width * self._height)

    def __str__(self):
        """Prints rectangle width/height"""
        return "[Rectangle] {}/{}".format(self._width, self._height)
