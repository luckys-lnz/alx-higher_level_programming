#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    big_score = None
    best_score = 0
    for key, value in a_dictionary.items():
        if value > best_score:
            best_score = value
            big_score = key
    return big_score
