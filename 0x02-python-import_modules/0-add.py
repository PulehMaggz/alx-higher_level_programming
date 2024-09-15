#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add  # Import the function without using *

    a = 1  # First variable assignment
    b = 2  # Second variable assignment

    # Using string formatting to print the result as required
    print(f"{a} + {b} = {add(a, b)}")
