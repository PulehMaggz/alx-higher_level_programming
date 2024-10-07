#!/usr/bin/python3
"""
Defines Change representation
"""
class Rectangle:
    """Representation of a rectangle."""
    
    number_of_instances = 0  # Class attribute to count instances
    print_symbol = "#"  # Class attribute for symbol used in string representation

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment instance count

    @property
    def width(self):
        """Getter for the private instance attribute width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the private instance attribute width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the private instance attribute height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the private instance attribute height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle using print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return (str(self.print_symbol) * self.__width + '\n') * (self.__height - 1) + str(self.print_symbol) * self.__width

    def __repr__(self):
        """Returns a string representation of the rectangle for eval."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Destructor that prints a message when an instance is deleted."""
        Rectangle.number_of_instances -= 1  # Decrement instance count
        print("Bye rectangle...")
