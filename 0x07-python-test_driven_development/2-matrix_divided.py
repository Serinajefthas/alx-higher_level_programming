#!/usr/bin/python3
"""Function divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Function divides all elements of matrix.

    Args:
        matrix (list): A list of lists of integers/floats
        div (int/float): Value which divides matrix

    Raises:
        TypeError:  If matrix is not a list of lists of integers or floats.
                    If each row of the matrix isn't of the same size.
                    If an element of any list is not an integer or float.
                    If a row in the matrix is not a list.
                    If div is not an integer or a float.
        ZeroDivisionError: If div is  0.

    Returns:
        matrix: new matrix with result of the division.
    """
    row_size = 0
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(error_msg)

    for i in matrix:
        if not i or not isinstance(i, list):
            raise TypeError(error_msg)

        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError(error_msg)

        if row_size != 0 and len(i) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(j / div, 2) for j in i] for i in matrix]

    return new_matrix
