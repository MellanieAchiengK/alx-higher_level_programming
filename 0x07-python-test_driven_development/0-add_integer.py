#!/usr/bin/python3
"""
Finds sum of two integers or floats
"""


def add_integer(a, b=98):
    """ function to find sum of two integers or floats """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        return TypeError("a must be an integer")

    if type(b) != int:
        return TypeError("b must be an integer")

    return a + b
