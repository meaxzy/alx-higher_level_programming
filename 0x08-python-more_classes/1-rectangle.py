#!/usr/bin/python3


"""A class that defines a rectangle."""
class Rectangle:
    def __init__(self, width=0, height=0):
        """ Initialize private attributes for width and height """
        self.__width = 0
        self.__height = 0
       
        """ Call the property setters to validate and set the width and height """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter method for width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method for width attribute """
        if type(value) is not int:
            """ Check if the input is an integer, raise an exception if not """
            raise TypeError("width must be an integer")
        if value < 0:
            """ Check if the input is non-negative, raise an exception if not """
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter method for height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method for height attribute """
        if type(value) is not int:
            """ Check if the input is an integer, raise an exception if not """
            raise TypeError("height must be an integer")
        if value < 0:
            """ Check if the input is non-negative, raise an exception if not """
            raise ValueError("height must be >= 0")
        self.__height = value
