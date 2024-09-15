#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # Use dir() to list all names defined in the hidden_4 module
    names = dir(hidden_4)
    
    # Filter out names that start with "__"
    filtered_names = [name for name in names if not name.startswith("__")]
    
    # Sort the names in alphabetical order
    for name in sorted(filtered_names):
        print(name)  # Print each name on a new line
