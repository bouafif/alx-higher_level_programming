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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method that writes the JSON string representation
        of list_objs to a file.
        Args:
            list_objs (list): List of instances to be serialized to JSON.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Static method that returns the list of the JSON string
        representation json_string.
        Args:
            json_string (str): JSON string representation
            of a list of dictionaries.
        Returns:
            list: List of instances represented by the JSON string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)
