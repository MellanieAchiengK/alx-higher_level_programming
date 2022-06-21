#!/usr/bin/python3
"""
Defines class Square """

class Square:
    """ define private instant attribute """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """ returns area of the square """
    def area(self):
        return self.__size * self.__size
