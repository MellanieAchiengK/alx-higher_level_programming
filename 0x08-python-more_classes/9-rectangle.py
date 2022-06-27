#!/usr/bin/python3
"""
Class Rectangle with width and height
"""


class Rectangle:
    """ class variable, counting number of instances """
    number_of_instances = 0

    """ class variable, symbol to print Rectangle """
    print_symbol = '#'

    """ Rectangle properties initialization """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances +=1

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

    """ returns a Rectangle instance with bigger area """
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    """ returns a Rectangle instance with equal width and height """
    @classmethod
    def square(cls,size=0):
        return cls(width=size, height=size)

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
        return "".join(rectangle)

    """ return a string representation of the rectangle
    to be able to recreate a new instance """
    def __rep__(self):
        wid = str(self.__width)
        hei = str(self.__height)

        rectangle = "Rectangle(" + wid + ", " + hei + ")"
        return rectangle

    """ prints a message for del """
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
