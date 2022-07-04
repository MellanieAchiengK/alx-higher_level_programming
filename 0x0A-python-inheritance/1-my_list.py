#!/usr/bin/python3
"""
class Mylist inherits from list
"""


class MyList(list):
    """ initializes Mylist """
    def __init__(self):
        pass

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
