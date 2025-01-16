#!/usr/bin/python3
"""Defines a class Square."""

class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square with optional size and position.
        
        Args:
            size (int): The size of the new square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).
        """
        self.size = size  # Use the setter for validation
        self.position = position  # Use the setter for position validation

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
            value (tuple): The position to set, must be a tuple of 2 positive integers.
        
        Raises:
            TypeError: If position is not a tuple of 2 integers.
            ValueError: If position integers are not positive.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character # to stdout, using position."""
        if self.__size == 0:
            print("")  # Print an empty line
        else:
            for i in range(self.__position[1]):  # Print leading empty lines
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
