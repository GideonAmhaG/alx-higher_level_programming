#!/usr/bin/python3
""" Module """


class Square:
    """ Square class """
    def __init__(self, size=0, position=(0, 0)):
        """ Initilize function """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Getter function """
        return self.__position

    @position.setter
    def position(self, position):
        """ Setter function """
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2 or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """ Returns are of the square """
        return self.__size * self.__size

    def my_print(self):
        """ Prints a square of # """
        if self.__size == 0:
            print()
        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print("")
        for j in range(0, self.area() + 1):
            if j % self.__size == 1:
                print("{:>{w}}".format("#", w=self.__position[0] + 1), end="")
            else:
                print("#", end="")
            if j % self.__size == 0:
                print()
