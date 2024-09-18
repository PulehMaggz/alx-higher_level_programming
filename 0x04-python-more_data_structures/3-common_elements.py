#!/usr/bin/python3

def common_elements(set_1, set_2):
    """Returns a set of common elements in two sets.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: A set containing common elements between set_1 and set_2.
    """
    return set_1 & set_2
