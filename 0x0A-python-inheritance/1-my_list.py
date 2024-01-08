#!/usr/bin/python3
""" Module for sorting a list"""


class MyList(list):
    """List class """
    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
