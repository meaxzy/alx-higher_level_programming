#!/usr/bin/python3
def no_c(my_string):
    for i in range(len(my_string)):
        if i == 'c' or i == 'C':
            continue
        print("{}".format(string[i]))
