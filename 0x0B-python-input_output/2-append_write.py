#!/usr/bin/python3
"""
append string
"""


def append_write(filename="", text=""):
    """ appends string at end of UTF8 file
    and returns number of characters added """

    with open(filename, mode="a", encoding="utf-8") as a_file:
        return a_file.write(text)
