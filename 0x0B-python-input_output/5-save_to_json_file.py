#!/usr/bin/python3
""" Save to json file module """
from json import dumps


def save_to_json_file(my_obj, filename):
    """" Writes an Object to a text file, using a JSON representation """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(dumps(my_obj))
