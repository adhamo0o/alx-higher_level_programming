#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix
    for i in range(len(matrix)):
        new_matrix = matrix[i] ** 2
    return new_matrix
