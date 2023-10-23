#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    print_integer = 0
    for print_integer in range(x):
        try:
            print("{}".format(my_list[print_integer]), end="")
        except IndexError:
            break
        print_integer = print_integer + 1
        print()

    return (print_integer)
