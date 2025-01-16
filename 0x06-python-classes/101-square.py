#!/usr/bin/python3
"""Defines a square by size and position, with area calculation and custom print behavior."""

class Square:
    """Represents a square."""
    
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square with a given size and position.
        
        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): A tuple of two positive integers representing the position. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Gets the position of the square."""
        return self.__position
    
    @position.setter
    def position(self, value):
        """Sets the position of the square with validation.
        
        Args:
            value (tuple): A tuple of two positive integers representing the position.
        
        Raises:
            TypeError: If position is not a tuple of two positive integers.
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) for i in value) or
            not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' character with specified position."""
        if self.__size == 0:
            print("")
        else:
            for y in range(self.__position[1]):
                print()  # Print vertical spaces
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Returns a string representation of the square for printing."""
        if self.__size == 0:
            return ""
        result = []
        for y in range(self.__position[1]):
            result.append("")  # Add vertical spaces
        for i in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(result)
