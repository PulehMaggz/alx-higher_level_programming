#!/usr/bin/python3
"""
This module contains a function that returns the list of available attributes
and methods of an object.
"""

def lookup(obj):
    """
    Returns a list of all attributes and methods of an object.
    
    Args:
        obj: The object whose attributes and methods will be listed.
    
    Returns:
        A list of available attributes and methods.
    """
    return dir(obj)
