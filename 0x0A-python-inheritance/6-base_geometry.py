#!/usr/bin/python3
"""Module for base geometry class"""


class BaseGeometry:
    """ A base geometry class """
    def area(self):
        """Raises exception if area is not implemented """
        raise Exception("area() is not implemented")
