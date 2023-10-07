#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        for i in range(len(my_list)):
            print("{:d} is {}".format(i, my_list[i]))
