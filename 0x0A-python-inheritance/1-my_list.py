#!/usr/bin/python3
"""defines an inherited list class Mylist"""


class Mylist(list):
    """implements sorted printing fot the built-in list class"""

    def print_sorted(self):
        """prints a list in a sorted ascending order """
        print(sorted(self))
