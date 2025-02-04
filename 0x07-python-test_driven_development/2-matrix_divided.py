#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix
by a given divisor and returns the resulting matrix rounded to two decimal places.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.
    
    Args:
        matrix (list of lists): A matrix of integers or floats.
        div (int or float): The divisor to divide all elements of the matrix.
    
    Returns:
        list of lists: The new matrix with divided values rounded to 2 decimal places.
    
    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows in matrix do not have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if len(matrix) > 0 and not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Create a new matrix with each element divided by div, rounded to 2 decimal places
    return [[round(element / div, 2) for element in row] for row in matrix]
