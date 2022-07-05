#!/usr/bin/python3
"""
checks for dictionary description
"""


def class_to_json(obj):
    """ returns dictionary description
    with simple data structure for JSON serialization of object """
    return obj.__dict__
