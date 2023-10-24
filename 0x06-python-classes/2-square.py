#!/usr/bin/python3
class Square:
    """ Defines a class Square """
    def __init__(self, size=0):
        """ Raise an error if not an integer """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        """ Raise an error if less than zero """
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
