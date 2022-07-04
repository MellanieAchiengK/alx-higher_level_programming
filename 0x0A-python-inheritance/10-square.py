#!/usr/bin/python3
"""
inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle

"""
Defines class Square
"""


class Square(Rectangle):
    """ initializes class """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    """ area of square """
    def area(self):
        return self.__size * self.__size
