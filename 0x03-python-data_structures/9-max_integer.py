#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    sorted_list = sorted(my_list)
    return sorted_list[-1]
