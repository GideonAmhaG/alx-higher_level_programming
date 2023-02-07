#!/usr/bin/python3
""" Pascal triangle module """


def pascal_triangle(n):
    """ Returns a list of lists of integers representing the Pascal’s
    triangle of n """
    triangle = [[1]]
    while len(triangle) != n:
        last_elem = triangle[-1]
        row = [1]
        for i in range(len(last_elem) - 1):
            row.append(last_elem[i] + last_elem[i + 1])
        row.append(1)
        triangle.append(row)
    return triangle
