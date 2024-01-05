#!/usr/bin/python3
""" Creates a locked class."""
class LockedClass:
    """
    Prevents any instatiation except from 'first_name'
    """

    __slots__ = ["first_name"]
