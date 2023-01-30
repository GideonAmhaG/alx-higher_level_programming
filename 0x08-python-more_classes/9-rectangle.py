#!/usr/bin/python3
""" Rectangle module """


class Rectangle:
    """ Rectangle class """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initilizing function """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ Getter function """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter function """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculates area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Calculates perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @classmethod
    def square(cls, size=0):
        """ Returns a new Rectangle instance with width == height == size """
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the biggest rectangle based on the area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """ Allows print to be called to print a rectangle of #s """
        s = ""
        if self.__width > 0 and self.__height > 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    s += str(self.print_symbol)
                s += "\n"
        return s[:-1]

    def __repr__(self):
        """ Generates a string representation of the rectangle to be able to
        recreate a new instance by using eval() """
        return "Rectangle({}, {})".format(self.__width, self.height)

    def __del__(self):
        """ Displays a message when when an instance of Rectangle is
        deleted """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
