#!/usr/bin/python3
"""class representing a square that inherits from rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class representing a Square that inherits from Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize Square instance with the provided size, x, y, and id values
        Width and height are set to the value of size. All attributes
        are validated using the same logic as in Rectangle.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter method for size attribute.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for size attribute.
        Sets width and height to the same value.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return a string representation of the Square instance in
        the format [Square] (<id>) <x>/<y> - <size>.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Square instance.

        Args:
            *args: List of arguments (no-keyworded).
                1st argument: id attribute.
                2nd argument: size attribute.
                3rd argument: x attribute.
                4th argument: y attribute.

            **kwargs: Dictionary of keyworded arguments.
                Key: Attribute to be updated (id, size, x, y).
                Value: New value for the attribute.

        Note:
            - If *args is provided, it will take precedence over **kwargs.
            - If *args exists and is not empty, **kwargs will be skipped.
        """
        if args:
            # Update attributes from *args
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            # Update attributes from **kwargs
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
