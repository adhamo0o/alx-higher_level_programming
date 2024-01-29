#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix[:]
    for i in range(len(matrix)):
        new_matrix = [[i ** 2 for i in j] for j in matrix]
    return new_matrix
