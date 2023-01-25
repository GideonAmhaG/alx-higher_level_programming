#!/usr/bin/python3
""" Mod """
import math


class MagicClass:
    """ Class """
    def __init__(self, radius=0):
        """ Func """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ Func """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ Func """
        return 2 * math.pi * self.__radius
