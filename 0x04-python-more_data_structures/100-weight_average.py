#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    sum_dividend = sum((items[0] * items[1]) for items in my_list)
    sum_divisor = sum(items[-1] for items in my_list)

    return sum_dividend / sum_divisor
