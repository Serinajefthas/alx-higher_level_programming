#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for element in range(len(matrix[row])):
                print("{}".format(element), end=" " if element != row[-1] else "")
        print()
