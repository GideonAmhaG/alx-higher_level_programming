#!/usr/bin/python3
""" Rectangle class module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Rectangle class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Class constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter function """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter function """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        if args:
            attr = ["id", "size", "x", "y"]
            for i, elem in enumerate(args):
                setattr(self, attr[i], elem)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square """
        my_dict = super().to_dictionary()
        my_dict["size"] = my_dict["width"]
        del my_dict["width"], my_dict["height"]
        return my_dict

    def __str__(self):
        """ Allows print to be called on Square """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                self.size)
