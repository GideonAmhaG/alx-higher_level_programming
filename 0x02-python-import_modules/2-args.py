#!/usr/bin/python3
import sys

if __name__ == "__main__":
    av = sys.argv
    prm = len(av) - 1

    if prm > 1:
        print(prm, "arguments:")
        for i in range(1, prm + 1):
            print("{:d}: {}".format(i, av[i]))
    elif prm == 1:
        print(prm, "argument:")
        for i in range(1, prm + 1):
            print("{:d}: {}".format(i, av[i]))
    elif prm == 0:
        print(prm, "arguments.")
