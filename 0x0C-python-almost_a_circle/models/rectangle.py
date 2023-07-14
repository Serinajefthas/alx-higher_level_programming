#!/usr/bin/python3
"""Defines a rectangle based on Base class

    Attributes:
        width (int): width of rectangle
        height (int): height of rectangle
        x (int): x value
        y (int): y value
    """


Base = __import__('base.py').Base


class Rectangle(Base):
    """Rectangle class
    Args:
        width (int): width of rectangle
        height (int): height of rectangle
        x (int): x value
        y (int): y value
        id (int): id from Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Get method to retrieve width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set method to set value of width attr"""
        self.__width = width

    @property
    def height(self):
        """Get method to retrieve height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Set method to set value of height attr"""
        self.__height = height

    @property
    def x(self):
        """Get method to retrieve x value"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Set method to set value of x attr"""
        self.__x = x

    @property
    def y(self):
        """Get method to retrieve y value"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Set method to set value of y attr"""
        self.__y = y
