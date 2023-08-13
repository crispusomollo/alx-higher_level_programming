#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        z = 0
        for y in range(len(x)):
            print("{:d}".format(x[y]), end=" " if y < len(x) - 1 else "\n")
            z += 1

    if len(matrix[0]) == 0:
        print("{}".format(""))
