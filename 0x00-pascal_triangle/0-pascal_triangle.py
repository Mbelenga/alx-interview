#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """ Pascal's Triangle """

    if n <= 0:
        return []

    pascal_triangle = [[1]]
    for index in range(1, n):
        row = [1]
        for j in range(1, index):
            val = pascal_triangle[index - 1][j - 1] + pascal_triangle[index - 1][j]
            row.append(val)
        row.append(1)
        pascal_triangle.append(row)
    return pascal_triangle

