#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """Area function
        Raises:
            Exception: if area is not implemented.
        """
        raise Exception("area() is not implemented")
