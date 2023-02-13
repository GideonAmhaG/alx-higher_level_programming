#!/usr/bin/python3
""" Base class module """
import json
from os import path


class Base:
    """ Manages id attribute in all future classes and avoids duplicating
    the same code (by extension, same bugs) """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        my_list = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for i in list_objs:
                my_list.append(i.to_dictionary())
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(my_list))

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            r = cls(1, 1)
        else:
            r = cls(1)
        r.update(**dictionary)
        return r

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        my_list = []
        filename = cls.__name__ + ".json"
        if path.isfile(filename):
            with open(filename, encoding="utf-8") as f:
                lists = cls.from_json_string(f.read())
            for i in lists:
                my_list.append(cls.create(**i))
        return my_list

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
