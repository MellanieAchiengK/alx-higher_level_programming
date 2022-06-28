#!/usr/bin/python3
"""
function to divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    checks matrix for a list of integers or floats
    matrix rows to be same size
    all elements of matrix should be divided by div
    and results returns a new matrix
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    result = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeErro("Each row of the matrix must have the same size")
        inner_list = []
        for items in lists:
            if not isinstance(items, (int, float)):
                raise TypeError(message)
            else:
                inner_list.append(round(items / div, 2))
        result.append(inner_list)

    return result
