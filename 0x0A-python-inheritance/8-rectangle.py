#!/usr/bin/python3
"""
Imports class BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""
Defines class Rectangle
"""


class Rectangle(BaseGeometry):
    """ initializes class """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
