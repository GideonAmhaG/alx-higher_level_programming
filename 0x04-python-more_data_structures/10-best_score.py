#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    best_score = max(a_dictionary.values(), default=None)

    for key, value in a_dictionary.items():
        if value == best_score:
            return key
