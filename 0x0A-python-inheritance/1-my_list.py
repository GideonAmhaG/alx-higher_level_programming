#!/usr/bin/python3
""" My list module """


class Mylist(list):
    """ A class that inherits from class list """
    def print_sorted(self):
        """ Prints the list, but sorted (ascending sort """
        print(sorted(self))
