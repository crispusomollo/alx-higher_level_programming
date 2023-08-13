#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        b = 0
        for c in range(len(a)):
            print("{:d}".format(a[b]), end=" " if b < len(a) - 1 else "\n")
            c += 1

    if len(matrix[0]) == 0:
        print("{}".format(""))
