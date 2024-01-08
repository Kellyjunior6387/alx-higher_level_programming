#!/usr/bin/python3
""" Module to invert functions"""


class MyInt(int):
    """ Class to rebel int """
    def __eq__(self, other):
        """ Inverts the == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """ Inverts the != operator"""
        return super().__eq__(other)
