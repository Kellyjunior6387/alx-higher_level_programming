#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        length = 0
        char = None
    length = len(sentence)
    char = sentence[0]
    return (length, char)
