#!/usr/bin/python3
""" Print square module """


def print_square(size):
    """ Prints a square with the character # """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print('', end='')
    else:
        for i in range(size):
            for j in range(size):
                print('#', end='')
            print()
