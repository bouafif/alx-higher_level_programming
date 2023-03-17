#!/usr/bin/python3
def best_score(a_dictionary):
    """returns a key with the biggest integer value."""

    if not isinstance(a_dictionary, dict):
        return None

    best_key = None
    best_value = None

    for key, value in a_dictionary.items():
        if (best_value is None or value > best_value):
            best_key = key
            best_value = value

    return best_key
