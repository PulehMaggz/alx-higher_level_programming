#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

# Additional test cases
print(max_integer([]))  # Test with an empty list
print(max_integer([-1, -5, -3, -4]))  # Test with all negative numbers
