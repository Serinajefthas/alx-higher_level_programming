#!/usr/bin/python3
"""Defines a square object based on Rectangle class

    Attributes:
        size (int): size of one side of square
        x (int): x value
        y (int): y value
    """


from .rectangle import Rectangle


class Square(Rectangle):
    """Square class
    Args:
        width (int): width of square
        height (int): height of square
        x (int): x value
        y (int): y value
        id (int): id of square; from Base class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Prints square (id) width/height"""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))

    @property
    def size(self):
        """Get method to retrieve size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """Set method to set value of size attr"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns arg or key/value pair to each variable"""
        prev_args = ["id", "size", "x", "y"]
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                if prev_args[i] == "size":
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, prev_args[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == "size":
                    setattr(self, "width", value)
                    setattr(self, "height", value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary rep of square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y", self.y,
        }
