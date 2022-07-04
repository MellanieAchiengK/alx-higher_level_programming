#!/usr/bin/python3
"""
checks if object is an instance of a class that inherited
(directly or indirectly) from specified class
"""


def inherits_from(obj, a_class):
    """ returns True if instance of a class """
    if type(obj) is a_class or not isinstance(obj, a_class):
        return False
    else:
        return True
