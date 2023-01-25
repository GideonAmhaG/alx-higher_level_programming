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
        if len(position) < 2 or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int) or \
                not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """ Returns are of the square """
        return self.__size * self.__size

    def my_print(self):
        """ Prints a square of # """
        if self.__size == 0:
            print()
        for i in range(0, self.area() + 1):
            if i == 0:
                for j in range(self.__position[0]):
                    print(" ", end="")
            else:
                print("#", end="")
                if i % self.__size == 0 and i > 0:
                    print()
                    if i < self.area():
                        for j in range(self.__position[0]):
                            print(" ", end="")
