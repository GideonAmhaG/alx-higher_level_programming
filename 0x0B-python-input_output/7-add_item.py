#!/usr/bin/python3
""" Add item module """
from os import path
from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
if path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []
for i in range(1, len(argv)):
    my_list.append(argv[i])
save_to_json_file(my_list, filename)
