#!/usr/bin/python3
"""
checks for object represented by a JSON string
"""


import json


def from_json_string(my_str):
    """ returns Python data structure represented by
    JSON string """
    return json.loads(my_str)
