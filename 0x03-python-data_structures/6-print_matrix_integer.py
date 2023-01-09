#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for items in matrix:
            i = 1;
            length = len(items)
            for item in items:
                if i == length:
                    print("{:d}".format(item), end="")
                else:    
                    print("{:d}".format(item), end=" ")
                i += 1
            print()
