#!/usr/bin/python3
""" Module that returns dictionary description with a simple
data structure for a JSON serialization of an object
"""


def class_to_json(obj):
    """Function that retuns the dictionary description of an obj. 

    Args:
        obj (MyClass): object

    Returns:
        dict: dictionary
    """
    return obj.__dict__
