#!/usr/bin/python3
def islower(c):
    """checks for lowercase"""
    if ord(c) > 96 and ord(c) < 123:
        return True
    else:
        return False
