#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    print_integer = 0
    for i in x:
        try:
            print("{}".format(my_list[i], end=""))
        except IndexError:
            break
        print_integer = print_integer + i
        print()

    return (print_integer)