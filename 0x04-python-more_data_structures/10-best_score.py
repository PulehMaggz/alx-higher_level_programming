#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns the key with the biggest integer value.

    Args:
        a_dictionary (dict): The dictionary with integer values.

    Returns:
        str: The key with the highest value, or None if the dictionary is empty or None.
    """
    if not a_dictionary:
        return None

    # Find the key with the maximum value
    return max(a_dictionary, key=a_dictionary.get)
