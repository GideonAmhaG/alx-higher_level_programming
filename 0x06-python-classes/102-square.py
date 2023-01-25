#!/usr/bin/python3
""" Module: Square class """


class Square:
    """ Square class """
    def __init__(self, size=0):
        """ Initilize function """
        self.size = size

    @property
    def size(self):
        """ Getter function """
        return self.__size

    @size.setter
    def size(self, size):
        """ Setter function """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Returns are of the square """
        return self.__size * self.__size

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
