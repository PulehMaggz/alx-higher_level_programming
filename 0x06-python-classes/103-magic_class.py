import math

class MagicClass:
    """A class to represent a circle with radius, area, and circumference."""
    
    def __init__(self, radius=0):
        """Initializes the radius and checks if it is a valid number (int or float)."""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area of the circle (π * r^2)."""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Returns the circumference of the circle (2 * π * r)."""
        return 2 * math.pi * self.__radius
