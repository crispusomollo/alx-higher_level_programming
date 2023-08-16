#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix1 = []
    for x in range(len(matrix)):
        matrix1.append(list(map(lambda x: x**2, matrix[x])))
    return matrix1
