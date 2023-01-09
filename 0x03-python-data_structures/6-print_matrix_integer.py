#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for items in matrix:
            for item in items:
                print("{:d}".format(item), end=" ")
            
            print()
