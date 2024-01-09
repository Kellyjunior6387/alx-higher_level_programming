#!/usr/bin/python3
"""Module that defines a class Student."""


class Student:
    """Class to represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
        Args:
            first_name (str):  first name
            last_name (str):  last name
            age (int):  age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the Student."""
        return self.
