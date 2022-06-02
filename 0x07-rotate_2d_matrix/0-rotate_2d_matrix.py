#!/usr/bin/python3
"""
This module contains a function that rotates a 2D matrix by 90 degrees
in a clockwise direction
"""


def rotate_2d_matrix(matrix):
    """function that rotates a 2D matrix by 90 degrees"""
    n = len(matrix)
    for i in range(n - 1):
        for j in range(i, n - 1 - i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp
