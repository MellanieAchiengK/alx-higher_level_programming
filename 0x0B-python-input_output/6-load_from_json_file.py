#!/usr/bin/python3
"""
object file from JSON file
"""


import json


def load_from_json_file(filename):
    """ creates Object from a "JSON file" """
    with open(filename, mode="r", encoding="UTF-8") as l_file:
        return json.load(l_file)
