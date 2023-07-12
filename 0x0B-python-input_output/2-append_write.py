#!/usr/bin/python3
""" Module that contains a function that appends to a text file
"""


def append_write(filename="", text=""):
    """ Function that appends to a text file

    Args:
        filename: filename
        text: text to write
    """
    if filename == "":
        filename = "new_file.txt"
    with open(filename, 'a') as file:
        return (file.write(text))
