#!/usr/bin/python3
def no_c(my_string):
    for item in range(97, 123):
        for item in range(65, 91):
            if item == 99 or item == 67:
                continue
            for i in my_string:
                print("{}".format(string[i]))
