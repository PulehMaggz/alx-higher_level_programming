# Python Inheritance - Lookup Function

## Description

This project implements a function `lookup()` that returns the list of all attributes
and methods of an object. This is a basic exercise to learn about Python's class inheritance
and how to interact with an object's methods and attributes.

## Usage

To use the `lookup()` function, simply pass an object to it, and it will return a list
containing the names of all the attributes and methods.

## Example

```python
class MyClass():
    pass

obj = MyClass()
print(lookup(obj))

# MyList Class - Inheritance from List

## Description

This project defines a class `MyList` that inherits from the built-in Python `list` class.
The `MyList` class adds a method `print_sorted` which prints the list sorted in ascending order.

## Usage

```python
from 1-my_list import MyList

my_list = MyList()
my_list.append(3)
my_list.append(1)
my_list.append(2)
my_list.print_sorted()  # This will print the list sorted: [1, 2, 3]
