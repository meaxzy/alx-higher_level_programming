#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    print_integer = 0
    for print_integer in range(x):
        try:
            i = int(print_integer)
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            break
        print_integer = print_integer + 1
    print("")

    return (print_integer)
