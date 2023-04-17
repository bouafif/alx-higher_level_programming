#!/usr/bin/python3
"""
Rectangle class that inherits from Base.
"""

from models.base import Base


class Rectangle(Base):
    """
    Class representing a Rectangle that inherits from Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): x-coordinate of the rectangle (default is 0).
            y (int): y-coordinate of the rectangle (default is 0).
            id (int): Id of the rectangle (default is None).
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for width attribute.

        Returns:
            int: Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width attribute.

        Args:
            value (int): New width value for the rectangle.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for height attribute.

        Returns:
            int: Height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height attribute.

        Args:
            value (int): New height value for the rectangle.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for x attribute.

        Returns:
            int: x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x attribute.

        Args:
            value (int): New x-coordinate value for the rectangle.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for y attribute.

        Returns:
            int: y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y attribute.

        Args:
            value (int): New y-coordinate value for the rectangle.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Print the Rectangle instance with the character '#' to stdout.
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)
