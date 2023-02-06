#!/usr/bin/python3
""" MyInt class module """


class MyInt(int):
    """ MyInt class """
    def __eq__(self, other):
        """ Inverts equal """
        return super(MyInt, self).__ne__(other)

    def __ne__(self, other):
        """ Inverts not equal """
        return super(MyInt, self).__eq__(other)
