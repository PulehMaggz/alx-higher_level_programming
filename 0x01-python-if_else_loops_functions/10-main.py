#!/usr/bin/env python3

# Import the add function from 10-add.py
add = __import__('10-add').add

# Test cases to verify the function
print(add(1, 2))        # Expected output: 3
print(add(98, 0))       # Expected output: 98
print(add(100, -2))     # Expected output: 98
