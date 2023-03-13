#!/usr/bin/python3
def multiple_returns(sentence):
    """returns a tuple with the length of a string and its first character."""

    length = len(sentence)
    if length == 0:
        return (0, None)
    first = sentence[0]
    return (len(sentence), sentence[0])
