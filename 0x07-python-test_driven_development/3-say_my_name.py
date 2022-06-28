#!/usr/bin/python3
"""
Function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """ prints first ame and last name
    checks if first_name and last_name are strings """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise Typeerror("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
