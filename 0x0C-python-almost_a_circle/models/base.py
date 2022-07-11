#!/usr/bin/python3
"""
base
"""
import json


class Base:
    """ base of all classes """
    #private class
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes JSON string representation of
        a list_objs to a file """
        filename = cls.__name__ + ".json"
        with open(filename, mode="w") as s_file:
            if list_objs is None:
                s_file.write("[]")
            else:
                s_file.write(cls.to_json_string(
                             [i.to_dictionary() for i in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """ returns list of JSON string
        representation """
        if json_string is None or len(json_string) == 0:
            return ("[]")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns instance with all set attributes """
        if cls.__name__ == "Rectangle":
            temp_instance = cls(3,3)
        elif cls.__name__ == "Square":
            temp_instance = cls(3)
        temp_instance.update(**dictionary)
        return temp_instance

    @classmethod
    def load_from_file(cls):
        """ returns list of instances """
        result = []
        filename = cls.__name__ + ".json"
        with open(filename, mode="r") as r_file:
            text = r_file.read()

        text = cls.from_json_string(text)
        for i in text:
            if type(i) == dict:
                result.append(cls.create(**i))
            else:
                result.append(item)
        return result
