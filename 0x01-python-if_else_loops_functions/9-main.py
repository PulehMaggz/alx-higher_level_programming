#!/usr/bin/env python3

# Import the print_last_digit function from 9_print_last_digit
from 9_print_last_digit import print_last_digit

# Test cases to check the function
print_last_digit(98)     # Expected output: 8
print()
print_last_digit(0)      # Expected output: 0
print()
r = print_last_digit(-1024)  # Expected output: 4
print()
print(r)                 # Expected output: 4 (as the return value of the function)
