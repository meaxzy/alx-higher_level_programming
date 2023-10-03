#!/usr/bin/python3
def print_last_digit(number):
    i = number % 10
    if number < 0:
        i = number % -10
    if i < 0:
        i = -i
    print("{}".format(i), end='')

    return i
