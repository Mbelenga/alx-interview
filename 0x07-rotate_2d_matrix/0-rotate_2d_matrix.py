#!/usr/bin/python3
""" Rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """ rotate matrix 90 degrees clockwise """
    n = len(matrix)
    for row in range(n):
        for column in range(row + 1, n):
            matrix[row][column], matrix[column][row] = (
                matrix[column][row], matrix[row][column]
                )
    for row in range(n):
        matrix[row].reverse()
