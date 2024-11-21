#!/usr/bin/python3

"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list[list[int]]): The n x n 2D matrix to rotate.

    Returns:
        None: The matrix is modified in-place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i + 1, n):  # Start at i+1 to avoid redundant swaps
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
