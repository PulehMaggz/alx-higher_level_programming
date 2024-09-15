#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div  # Correct import, only once

    a = 10  # Assigning value to variable a
    b = 5   # Assigning value to variable b

    # Print the results of each mathematical operation
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {sub(a, b)}")
    print(f"{a} * {b} = {mul(a, b)}")
    print(f"{a} / {b} = {div(a, b)}")
