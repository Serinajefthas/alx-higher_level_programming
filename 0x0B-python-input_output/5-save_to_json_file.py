#!/usr/bin/python3
""" Module that writes an Object to a text file using
a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ Function that writes an object to a text file
    by a JSON representation

    Args:
        my_obj: object
        filename: text file name
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json_obj = json.dumps(my_obj)
        file.write(json_obj)
