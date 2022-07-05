#!/usr/bin/python3
"""
Reads file
"""


def read_file(filename=""):
    """ reads text file(UTF8)
    and prints to stdout) """

    with open(filename, encoding="utf-8") as r_file:
        print(r_file.read(), end="")
