#!/usr/bin/python3
""" A function that Sorts and prints the list in ascending order. """


class MyList(list):
    """ new class named MyList, this class inherits from the list class. """

    def print_sorted(self):
        print(sorted(self))
