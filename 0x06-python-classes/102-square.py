#!/usr/bin/python3
"""Defines a square by its size, with area calculation and comparison operators."""

class Square:
    """Represents a square."""
    
    def __init__(self, size=0):
        """Initializes a square with a given size.
        
        Args:
            size (float or int): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.
        
        Args:
            value (float or int): The size to set.
        
        Raises:
            TypeError: If size is not a number (int or float).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2

    # Comparison operators based on area of the square
    def __eq__(self, other):
        """Checks if two squares are equal (same area)."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks if two squares are not equal (different areas)."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Checks if one square is smaller than the other (based on area)."""
        return self.area() < other.area()

    def __le__(self, other):
        """Checks if one square is smaller than or equal to the other (based on area)."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Checks if one square is greater than the other (based on area)."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks if one square is greater than or equal to the other (based on area)."""
        return self.area() >= other.area()
