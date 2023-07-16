#!/usr/bin/python3
"""Defines a square object based on Rectangle class

    Attributes:
        width (int): width of rectangle
        height (int): height of rectangle
        x (int): x value
        y (int): y value
    """


from .base import Base


class Rectangle(Base):
    """Rectangle class
    Args:
        width (int): width of rectangle
        height (int): height of rectangle
        x (int): x value
        y (int): y value
        id (int): id of rectangle; from Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
