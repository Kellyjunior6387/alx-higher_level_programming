#!/usr/bin/python3
"""Module  to test parent"""


def is_same_class(obj, a_class):
    """Returns True if object is instance of the class"""
    if isinstance(obj, a_class):
        return True
    return False
