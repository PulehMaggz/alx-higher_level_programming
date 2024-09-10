#!/usr/bin/python3

def pow(a, b):
    """Return a to the power of b."""
    if b == 0:
        return 1
    elif b < 0:
        return 1 / (a ** -b)
    else:
        result = 1
        for _ in range(b):
            result *= a
        return result
