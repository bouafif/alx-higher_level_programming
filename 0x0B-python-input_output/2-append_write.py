#!/usr/bin/python3
"""defines function that appends a string at the end of a text file """


def append_write(filename="", text=""):
    """append text to the utf8 file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
