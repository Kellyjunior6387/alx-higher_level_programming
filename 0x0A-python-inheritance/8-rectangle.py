#!/usr/bin/python3
"""Module to demonstrate inheritance """


class BaseGeometry:
    """ Base geometry class"""
    def area(self):
        """Raises exception if area is not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ class rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width
