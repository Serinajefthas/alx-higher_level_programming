#!/usr/bin/python3
"""Returns list available methods and objects of
objects
"""


def lookup(obj):
    """Function that returns the list of available attributes and methods
     of object

    Args:
        obj (class): object

    Returns:
        list: list of available attributes and methods of object
    """
    attributelist = dir(obj)
    return attributelist
