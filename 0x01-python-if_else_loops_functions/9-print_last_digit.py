#!/usr/bin/python3
def print_last_digit(number):
    if(number < 0):
        i = number % -10
        if i < 0:
            i = -i
    else:
        i = number % 10
        print("{}".format(i))
