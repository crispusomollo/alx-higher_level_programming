#!/usr/bin/python3
"""
Module 2-matrix_divided
Has a method that divide all the elements of a matrix and return new matrix
Requires the same size lists of int or float, and max of two decimal places
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix with dividends
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(msg)

    new_matrix = []
    same_len = len(matrix[0])
    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(msg)
        if len(lists) != same_len:
            raise TypeError("Each row of the matrix must have the same size")
        new_list = []
        for i in lists:
            if not isinstance(i, (int, float)):
                raise TypeError(msg)
            new_list.append(round(i/div, 2))
        new_matrix.append(new_list)
    return new_matrix
