#!/usr/bin/python3
"""
Defines class Square """


class Square:
    """ defines private attribute """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        message = 'position must be a tuple of 2 positive integers'
        if type(value) != tuple:
            raise TypeError(message)
        if len(value) != 2:
            raise TypeError(message)

        for items in value:
            if type(items) != int:
                raise TypeError(message)
            if type(items) < 0:
                raise TypeError(message)

        self.__position = value

    """ returns area of the square """
    def area(self):
        return self.__size * self.__size

    """ prints square with # in stdout """
    def my_print(self):
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
