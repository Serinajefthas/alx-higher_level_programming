#!/usr/bin/python3
"""Defines a class Base"""

class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        self.__nb_objects += 1
        id = self.__nb_objects
