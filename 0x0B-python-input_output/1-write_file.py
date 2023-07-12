#!/usr/bin/python3
def write_file(filename="", text=""):
    if filename == "":
        filename = 'new_file.txt'
    with open(filename, 'w', encoding='utf-8') as file:
        nchars = file.write(text)
        return nchars
