#!/usr/bin/python3
""" Base class module """


class Base:
    """ Manages id attribute in all future classes and avoids duplicating
    the same code (by extension, same bugs) """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
