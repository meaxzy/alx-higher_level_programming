#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in range(len(row)):
            if i > 0:
                print(" ", end=" ")
            print("{:d}".format(num[i]), end="")
        print()
