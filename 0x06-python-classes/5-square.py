#!/usr/bin/python3
""" class Square that defines a square"""

class Square:
    """ class Square"""

    def __init__(self, size=0):
        """ initialize new square
        Args:
            size (int): size of the square
        """
        self.__size = size

    @property
    def size(self):
        """Get method to retrieve size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter to set value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Method returning area of current square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints square with # to stdout"""
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
