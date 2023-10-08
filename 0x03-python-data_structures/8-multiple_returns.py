#!/usr/bin/python3
def multiple_returns(sentence):
    for i in range(len(sentence)):
        if i == " ":
            return None
        else:
            return i, len(sentence[0])

