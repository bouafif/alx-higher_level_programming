#!/usr/bin/python3
"""function that writes a string to a text file"""


def write_file(filename="", text=""):
    """writes string and return value"""
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
