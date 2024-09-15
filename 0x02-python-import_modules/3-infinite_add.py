#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0  # Initialize total sum
    # Loop through the arguments (starting from index 1 to skip the script name)
    for arg in sys.argv[1:]:
        total += int(arg)  # Convert each argument to int and add to total
    
    print(total)  # Print the result
