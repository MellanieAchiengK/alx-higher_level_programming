#!/usr/bin/python3
"""
Define class Square
"""

class Square:
   """ define optional private size instant attribute """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """ returns area of square """
    def area(self):
        return self.__size * self.__size
