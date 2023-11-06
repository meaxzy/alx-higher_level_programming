#!/usr/bin/python3
""" Checks for same kind of object and class """


def is_kind_of_class(obj, a_class):

    """
    True if obj is an instance of a_class or its subclass; otherwise, False.
    Args:
        obj: The object to check.
        a_class: The class to compare with.

    """
    return isinstance(obj, a_class)
