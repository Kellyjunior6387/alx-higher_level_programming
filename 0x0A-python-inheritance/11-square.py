#!/usr/bin/python3
""" Module to show inheritance """


class BaseGeometry:
    """ Class for base geometry"""
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
    """Instantiate width and height"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        """ Method to calculate area"""
        return self.__height * self.__width

    def __str__(self):
        """Returns representation as a string """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """ Instantiate size of a sqaure"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Method to calculate area"""
        return self.__size * self.__size

    def __str__(self):
        """Returns representation as a string """
        return f"[Square] {self.__size}/{self.__size}"
