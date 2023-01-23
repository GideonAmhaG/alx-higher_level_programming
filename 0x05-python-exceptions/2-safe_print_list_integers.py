#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for item in my_list:
        try:
            if type(item) is int and counter != x:
                print("{:d}".format(item), end="")
                counter += 1
        except TypeError:
            continue
    print()
    return counter
