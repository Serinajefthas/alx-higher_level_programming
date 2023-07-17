#!/usr/bin/python3
"""Defines a class Base"""


class Base:
    """Base class
    Args:
        __nb_objects (int): private num objects attr
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Base constructor, initilise new obj
        Args:
            id (int): id of the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
