#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for key  in a_dictionary:
        if key in a_dictionary:
            del a_dictionary[key]
