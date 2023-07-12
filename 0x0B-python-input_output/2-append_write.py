#!/usr/bin/python3
def append_write(filename="", text=""):
    if filename == "":
        filename = "new_file.txt"
    with open(filename, 'a') as file:
        return (file.write(text))
