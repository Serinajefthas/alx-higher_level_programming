#!/usr/bin/python3
""" Module that creates an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """ Function that creates an Object from a JSON file

    Args:
        filename: text file name
    Returns:
        object: object
    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
