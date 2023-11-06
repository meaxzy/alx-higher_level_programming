#!/usr/bin/python3


""" Check instance of the object if same """
def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class; otherwise, False.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if obj is an instance of a_class; otherwise, False.
    """
    return type(obj) == a_class
