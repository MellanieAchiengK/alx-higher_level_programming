#!/usr/bin/python3
"""
write object using JSON
"""


import json


def save_to_json_file(my_obj, filename):
    """ writes Object to text file using JSON representation """
    with open(filename, mode="w", encoding="UTF-8") as s_file:
        s_file.write(json.dumps(my_obj))
