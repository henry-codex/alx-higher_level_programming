#!/usr/bin/python3
def multiple_returns(sentence):
    size_str = len(sentence)
    try:
        first_letter = sentence[0]
    except IndexError:
        first_letter = None
    return size_str, first_letter
