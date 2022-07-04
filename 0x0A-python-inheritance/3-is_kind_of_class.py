#!/usr/bin/python3
"""
checks if object is an instance of,
is an instance of a class that inherited from,
the specified class
"""


def is_kind_of_class(obj, a_class):
    """ returns true if object us an instance of a class
    or class inherited from the class """

    if isinstance(obj, a_class):
        return True
    else:
        return False
