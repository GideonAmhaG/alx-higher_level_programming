#!/usr/bin/python3
""" Rectangle class module """


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class """
    def __init__(self, width, height):
        """ Initilizing function """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Returns area """
        return self.__width * self.__height

    def __str__(self):
        """ Allows print to be called on Rectangle class """
        return "[Rectangle] {}/{}".format(self.__width, self. __height)
