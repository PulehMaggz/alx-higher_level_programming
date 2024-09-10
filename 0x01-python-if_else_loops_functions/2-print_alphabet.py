#!/usr/bin/python3

# Use a single loop to print all lowercase letters from 'a' to 'z'
print(''.join(chr(i) for i in range(ord('a'), ord('z') + 1)), end='')
