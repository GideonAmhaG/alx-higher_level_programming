#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    av = sys.argv
    prm = len(av) - 1

    if prm == 3:
        op = av[2]
        a = int(av[1])
        b = int(av[2])

        if op == "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
            exit(0)
        if op == "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
            exit(0)
        if op == "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
            exit(0)
        if op == "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
