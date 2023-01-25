#!/usr/bin/python3
""" Module """


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

    def my_print(self):
        """ Prints a square of # """
        if self.__size == 0:
            print()
        for i in range(1, self.area() + 1):
            print("#", end="")
            if i % self.__size == 0:
                print()
