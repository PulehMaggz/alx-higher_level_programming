#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix.

    Args:
        matrix (list of lists of ints): A 2D array of integers.

    Returns:
        list of lists of ints: A new matrix with squared values.
    """
    return [[x ** 2 for x in row] for row in matrix]
