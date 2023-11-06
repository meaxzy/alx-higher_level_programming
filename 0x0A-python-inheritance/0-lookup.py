#!/usr/bin/python3
"""list of available attributes and methods of an object"""


def lookup(obj):
     """Return a list of available attributes and methods of an object"""
     
     class MyClass1(object):
         pass

     class MyClass2(object):
         my_attr1 = 3
         def my_meth(self):
             pass
