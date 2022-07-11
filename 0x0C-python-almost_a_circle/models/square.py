#!/usr/bin/python3
"""
class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """ size Getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size Setter """
        self.width = value
        self.height = value

    def __str__(self):
        """ __str__ method """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width))

    def update(self, *args, **kwargs):
        """ updates attributes """
        if len(args) != 0:
            i = 0
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                    self.height = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                if key == "size":
                    self.width = kwargs[key]
                    self.height = kwargs[key]
                if key == "x":
                    self.x = kwargs[key]
                if key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        """ returns dictionary representation of Square """
        return {'id': self.id, 'size': self.width,
                'x': self.x, 'y': self.y}
