#!/usr/bin/env python3

# Import the pow function from 11-pow.py
pow = __import__('11-pow').pow

# Test cases to verify the function
print(pow(2, 2))      # Expected output: 4
print(pow(98, 2))     # Expected output: 9604
print(pow(98, 0))     # Expected output: 1
print(pow(100, -2))   # Expected output: 0.0001
print(pow(-4, 5))     # Expected output: -1024
