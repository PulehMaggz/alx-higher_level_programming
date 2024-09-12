#!/usr/bin/python3

# Import all functions from calculator_1
from calculator_1 import add, sub, mul, div

# Define variables a and b
a = 10
b = 5

# Call each function and print the results
print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))
