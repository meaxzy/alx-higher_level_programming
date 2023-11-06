#!/usr/bin/python3
""" Define class called BaseGeometry """


class BaseGeometry:
    """ Defining class with atrributes and methods """

    def area(self):

        """
        Calculate the area (not implemented).

        """
    raise Exception ("area() is not implemented")

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """ Validate width and height using the integer_validator method """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        """ Set private attributes"""
        self.__width = width
        self.__height = height
