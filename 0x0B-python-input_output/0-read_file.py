#!/usr/bin/python3
""" defines a text file-reading function"""


def read_file(filename=""):
    """print the contentof a UTF8 file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
