#!/usr/bin/python3
"""Defines function that prints text with 2 new lines after .?: characters
"""


def text_indentation(text):
    """Prints a text with 2 new lines after .?: characters

    Args:
        text (str): string to be modified

    Raises:
        TypeError: If text is not of type string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")
