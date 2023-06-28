#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    new_matrix = []
    for row in matrix:
        new_matrix.append([elem**2 for elem in row if isinstance(elem, int)])
    return (new_matrix)
