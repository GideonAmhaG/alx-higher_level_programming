#!/usr/bin/python3
""" Rectangle module """


class Rectangle:
    """ Rectangle class """
    def __init__(self, width=0, height=0):
        """ Initilizing function """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter function """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter function """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """ Getter function """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter function """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
