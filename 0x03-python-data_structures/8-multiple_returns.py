#!/usr/bin/python3
def multiple_returns(sentence):
    for i in range(len(sentence)):
        if sentence[i] == "":
            return None
        else:
            return (sentence[i], sentence[0])
