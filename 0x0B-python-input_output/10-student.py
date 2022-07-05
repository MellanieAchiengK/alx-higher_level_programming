#!/usr/bin/python3
"""
class Student
"""


class Student:
    """ defines student data """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """ retrieves dictionary representation """
    def to_json(self, attrs=None):
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        else:
            newdict = {}
            for elm in attrs:
                if type(elm) != str:
                    return self.__dict__
                if elm in self.__dict__.keys():
                    newdict[elm] = self.__dict__[elm]
            return newdict
