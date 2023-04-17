#!/usr/bin/python3
"""
Base class for managing id attribute in all other classes in the project.
"""

class Base:
    """
    Base class for managing id attribute in all other classes in the project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for Base class.

        Args:
            id (int): ID value for the object. If not provided, a unique ID
                      will be generated.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
