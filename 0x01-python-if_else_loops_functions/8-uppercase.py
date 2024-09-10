#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            # Convert to uppercase
            print(chr(ord(char) - 32), end="")
        else:
            # Print the character as is
            print(char, end="")
    print()  # Print a new line at the end
