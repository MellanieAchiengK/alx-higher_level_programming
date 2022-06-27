#!/usr/bin/python3
"""
Class Rectangle with width and height
"""


class Rectangle:
    """ Rectangle properties initialization """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width Setter """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height Setter """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """ returns area of the rectangle """
    def area(self):
        return self.__width * self.__height

    """ returns perimeter of the rectangle """
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    """ prints rectangle with # """
    def __str__(self):
        rectangle = []
        if self.__width == 0 or self.__height == 0:
            return rectangle
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    rectangle.append("#")
                if i < self.__height - 1:
                    rectangle.append("\n")
        return ("".join(rectangle))
