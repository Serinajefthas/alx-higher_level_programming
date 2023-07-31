#!/usr/bin/python3
""" Module containing a function that adds two integers"""


def add_integer(a, b=98):
    """ Function adds two integers/float numbers

    Args:
        a: first number
        b: second number

    Returns:
        The addition of the two given numbers

    Raises:
        TypeError: If a or b aren't integer/float numbers

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
