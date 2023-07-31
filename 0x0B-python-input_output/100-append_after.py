#!/usr/bin/python3
"""Module that contains the function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """Function that inserts a line of text to a file, after each line,
    containing specific string.

    Args:
        filename (str, optional): name of file
        search_string (str, optional): string to search
        new_string (str, optional): string to append
    """
    with open(filename, "r") as f:
        text = f.readlines()

    with open(filename, "w") as fi:
        s = ""
        for line in text:
            s += line
            if search_string in line:
                s += new_string
        fi.write(s)
