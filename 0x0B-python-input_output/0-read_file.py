#!/usr/bin/python3
""" Function that reads a text file and print it"""


def read_file(filename=""):
    """ Read file and print it"""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
