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
        if self.size == 0:
            print()
        else:
            x = self.position[0]
            y = self.position[1]
            for i in range(y):
                print("")
            for row in range(self.size):
                for j in range(x):
                    print(" ", end="")
                for col in range(self.size):
                    print("#", end="")
                print()
