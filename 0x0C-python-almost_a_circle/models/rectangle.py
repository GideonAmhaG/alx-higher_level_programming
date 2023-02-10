#!/usr/bin/python3
""" Rectangle class module """


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
        if value <= 0:
            raise ValueError("x must be > 0")
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
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value
