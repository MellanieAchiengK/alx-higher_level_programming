#!/usr/bin/python3
"""
checks if an object is exactly an instance of a class
"""


def is_same_class(obj, a_class):
    """ returns true if object is same as instance """
    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    else:
        return False
