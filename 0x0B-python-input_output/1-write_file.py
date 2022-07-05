#!/usr/bin/python3
"""
module to write string to text file
"""


def write_file(filename="", text=""):
    """ writes string to UTF8 file and
    returns number of characters written """

    with open(filename, mode="w", encoding="utf-8") as w_file:
        return w_file.write(text)
