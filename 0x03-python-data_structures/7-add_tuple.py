#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = checkt(tuple_a)
    tuple_b = checkt(tuple_b)

    return(tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])


def checkt(tup=()):
    if len(tup) < 2:
        if len(tup) == 1:
            tup = (tup[0], 0)
        elif len(tup) == 0:
            tup = (0, 0)
    elif len(tup) > 2:
        tup = (tup[0], tup[1])
    return tup
