#!/usr/bin/python3
"""Function that prints square using '#' character"""


def print_square(size):
    """ Function that prints a square with the character #

    Args:
        size: size of the square

    Raises:
        TypeError: If size is not an integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
