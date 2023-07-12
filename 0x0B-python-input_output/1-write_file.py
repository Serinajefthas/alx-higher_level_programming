#!/usr/bin/python3
""" Module that contains function that writes text to file """


def write_file(filename="", text=""):
    """ Function that writes to a file

    Args:
        filename: filename
        text: text to append to file
    
    Returns:
        int: number chars written to file
    """
    if filename == "":
        filename = 'new_file.txt'
    with open(filename, 'w', encoding='utf-8') as file:
        nchars = file.write(text)
        return nchars
