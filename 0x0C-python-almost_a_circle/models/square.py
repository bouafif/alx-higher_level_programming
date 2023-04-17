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

    def __str__(self):
        """
        Return a string representation of the Square instance in
        the format [Square] (<id>) <x>/<y> - <size>.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
