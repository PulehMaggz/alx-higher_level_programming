#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))          # Should print the type of the object
print(my_rectangle.__dict__)      # Should print an empty dictionary {}
