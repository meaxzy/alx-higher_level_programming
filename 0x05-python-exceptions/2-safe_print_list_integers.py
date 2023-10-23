#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    print_integer = 0
    for i in range(x):
        try:
            y = my_list[i]
            integer = int(y)
            print("{:d}".format(integer), end="")
        except (ValueError, TypeError):
            break
        print_integer = print_integer + 1
    print("")

    return (print_integer)
