#!/usr/bin/python3
"""Defines a class Square."""

class Square:
    """Represents a square."""
    
    def __init__(self, size=0):
        """Initializes a new square.
        
        Args:
            size (int): The size of the new square. Defaults to 0.
        """
        self.size = size  # Use the setter for validation

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.
        
        Args:
            value (int): The size to set.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size ** 2
