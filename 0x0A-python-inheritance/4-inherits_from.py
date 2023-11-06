#!/usr/bin/python3
""" Check if the object is an instance of a class that inherited """


def inherits_from(obj, a_class):

    """
    Check if an object is an instance of a class that inheritedform a class

    Args:
        obj: The object to check.
        a_class: The class to compare inheritance with.

    """
    return issubclass(type(obj), a_class)
