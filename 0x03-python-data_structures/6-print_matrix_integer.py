#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for indx in (matrix):
        for indy in range(len(indx)):
            if indy < len(indx) - 1:
                print("{:d} ".format(indx[indy]), end='')
            else:
                print("{:d}".format(indx[indy]), end='')
        print()
