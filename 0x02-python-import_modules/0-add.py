#!/usr/bin/python3
import add_0 as plus
def add(a, b):
    a = 1
    b = 2

    result = plus.add(a, b)
    print("{} + {} = {}".format(a, b, result), end='')
