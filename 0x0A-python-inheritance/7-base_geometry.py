#!/usr/bin/python3

class BaseGeometry:
    def area(self):
        """Raises exception if area is not implemented """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ Validates value """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

