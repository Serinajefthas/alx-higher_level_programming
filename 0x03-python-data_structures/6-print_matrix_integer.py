#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for element in range(len(matrix[row])):
            if element == len(matrix[row]) -1:
                print("{}".format(matrix[row][element]), end="")
            else:
                print("{}".format(matrix[row][element]), end=" ")
        print()
