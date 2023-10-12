#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    highest_score = None
    for key in a_dictionary:
        if highest_score is None or a_dictionary[key] > highest_score:
            highest_score = a_dictionary[key]
    return highest_score
