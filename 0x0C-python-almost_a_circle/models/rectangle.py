#!/usr/bin/python3
"""Defines a rectangle based on Base class

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

    @property
    def width(self):
        """Get method to retrieve width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set method to set value of width attr"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get method to retrieve height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Set method to set value of height attr"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get method to retrieve x value"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Set method to set value of x attr"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get method to retrieve y value"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Set method to set value of y attr"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Prints rectangle to stdout using '#' char"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        for i in range(self.height + self.y):
            if i >= (self.y):
                print(" " * self.x + "#" * self.width)
            else:
                print(" " * self.x)

    def __str__(self):
        """Prints rectangle width/height"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Assigns arg or key/value pair to each variable"""
        prev_args = [self.__width, self.__height, self.__x, self.__y]
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, prev_args[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
