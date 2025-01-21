#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list class
and includes a method to print the list in sorted order.
"""

class MyList(list):
    """
    MyList class that inherits from the built-in list.
    It adds a method to print the list in sorted order.
    """
    
    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))
