#!/usr/bin/python3
""" Rectangle class module """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter function """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter function """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter function """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter function """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter function """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter function """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter function """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter function """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ Prints in stdout the Rectangle instance with the character # """
        if self.__y > 0:
            print("\n" * self.__y, end="")
        for i in range(self.__height):
            if self.__x > 0:
                print(" " * self.__x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        if args:
            attr = ["id", "width", "height", "x", "y"]
            for i, elem in enumerate(args):
                if i < len(attr):
                    setattr(self, attr[i], elem)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle """
        my_dict = {}
        for key, value in self.__dict__.items():
            short_key = key.split("__")[-1]
            my_dict[short_key] = value
        return my_dict

    def __str__(self):
        """ Allows print to be called on Rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)
