#!/usr/bin/python3
"""
class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width Setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x Getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x Setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y Getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y Setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns area of rectangle """
        return self.__width * self.__height

    def display(self):
        """ prints Rectangle to stdout using # """
        for y in range(self.__y):
            print("")
        for i in range(self.__height):
            print(" "*self.__x + "#"*self.__width)

    def __str__(self):
        """ __str__ function """
        return ("[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                 self.id, self.__x,
                                                 self.__y, self.__width,
                                                 self.__height))

    def update(self, *args, **kwargs):
        """ updates attribute """
        if len(args) != 0:
            i = 0
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.__width = args[i]
                elif i == 2:
                    self.__height = args[i]
                elif i == 3:
                    self.__x = args[i]
                elif i == 3:
                    self.__y = args[i]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "width":
                    self.__width = kwargs[key]
                elif key == "height":
                    self.__height = kwargs[key]
                elif key == "x":
                    self.__x = kwargs[key]
                elif key == "y":
                    self.__y = kwargs[key]

    def to_dictionary(self):
        """ returns dictionary representation of Rectangle """
        return {'id': self.id, 'width': self.__width, 
                'height': self.__height, 'x': self.__x, 'y': self.__y}
