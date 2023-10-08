#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        pass
    else:
        for row in matrix:
            for i in range(len(row)):
                if i > 0:
                    print(" ", end=" ")
                else:
                    print("{:d}".format(row[i]), end="")
        print()
