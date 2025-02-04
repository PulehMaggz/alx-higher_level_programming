#!/usr/bin/python3
"""
This module provides a function add_integer() that adds two integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.
    
    Args:
        a: The first integer or float.
        b: The second integer or float (defaults to 98).
        
    Returns:
        The sum of a and b as an integer.
        
    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if ((not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    
    # Cast floats to integers before adding
    return int(a) + int(b)
