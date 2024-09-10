#!/usr/bin/python3

for i in range(97, 123):  # ASCII values for 'a' to 'z'
    if chr(i) not in ('q', 'e'):
        print(chr(i), end='')
