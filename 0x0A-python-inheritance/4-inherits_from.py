#!/usr/bin/python3
"""defines an inherited class-checking function"""


def inherits_from(obj, a_class):
    """checks if an object is an inherited instance of a class
    Args:
    obj (any): the object to check
    a_class (type): the class to match the type of obj to
    Returns:
    if obj is an inherited instance of a_class - True
    otherwise - False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
