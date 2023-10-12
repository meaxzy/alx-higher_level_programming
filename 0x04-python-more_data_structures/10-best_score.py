#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary = {}:
        return None
    highest_score = a_dictionary[0]
    for x in range (1, len(a_dictionary)):
        if a_dictionary[x] > highest_score:
            highest_score = a_dictionary[x]
    return highest_score
