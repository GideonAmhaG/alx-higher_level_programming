#!/usr/bin/python3
""" From json string module """
from json import loads


def from_json_string(my_str):
    """" Returns an object (Python data structure) represented by a JSON
    string """
    return loads(my_str)
