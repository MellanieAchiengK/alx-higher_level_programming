#!/usr/bin/python3
class Square:
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

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            x = self.__position[0]
            y = self.__position[1]
            for i in range(y):
                print("")
            for row in range(self.__size):
                for j in range(x):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
