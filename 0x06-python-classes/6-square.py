#!/usr/bin/python3
""" class Square that defines a square"""

class Square:
    """ class Square"""

    def __init__(self, size=0, position=(0,0)):
        """ initialize new square
        Args:
            size (int): size of the square
            position (int, int): position of square in co-ordinates
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Get current position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter property for position of square
        Args:
            value (tuple): position of the square.
        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Method returning area of current square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints square with # to stdout"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for j in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end='')
                print("#" * self.__size)

