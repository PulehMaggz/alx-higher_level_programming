# Square Matrix Simple

## Description

This project contains a Python function that computes the square value of all integers in a 2D matrix. The function returns a new matrix with the squared values, leaving the original matrix unchanged.

## Files

1. `0-square_matrix_simple.py`: Contains the `square_matrix_simple` function that takes a 2D matrix and returns a new matrix where each element is the square of the original element.

2. `0-main.py`: A test script that demonstrates the usage of the `square_matrix_simple` function. It prints the new squared matrix and the original matrix to show that the original matrix remains unchanged.

## Function Prototype

```python
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.
    
    Args:
        matrix (list of lists of ints): A 2D array of integers.
        
    Returns:
        list of lists of ints: A new matrix with squared values.
    """
    return [[x ** 2 for x in row] for row in matrix]
