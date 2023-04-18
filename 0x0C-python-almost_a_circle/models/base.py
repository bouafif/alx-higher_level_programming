#!/usr/bin/python3
"""
Base class for managing id attribute in all other classes in the project.
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
