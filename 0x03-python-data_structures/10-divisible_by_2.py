#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    value = []
    for num in my_list:
        if num % 2 == 0:
            value.append(True)
        else:
            value.append(False)
    return value
