#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Returns a list with True or False, depending on whether the integer at the same position in the original list is a multiple of 2."""
    return [item % 2 == 0 for item in my_list]
