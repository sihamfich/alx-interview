#!/usr/bin/python3
"""
0-pascal_triangle.py
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the 'n' rows.

    Args:
        n (int): The number of rows in Pascal's Triangle.

    Returns:
        List[List[int]]: A list of lists where each sublist represents
                          a row in Pascal's Triangle.
    """
    # Initialize the matrix to hold the rows of Pascal's Triangle
    matrix = []

    # Edge case: If n is less than or equal to 0, return an empty list
    if n <= 0:
        return matrix

    # Base case: the first row is always [1]
    matrix.append([1])

    # Generate subsequent rows
    for i in range(1, n):
        # Start with a row with the first element as 1
        current_row = [1]

        # Get the previous row from the matrix
        previous_row = matrix[i - 1]

        # Generate the elements of the current row based on the previous row
        for j in range(1, i):
            current_row.append(previous_row[j - 1] + previous_row[j])

        # End the row with a 1
        current_row.append(1)

        # Append the completed row to the matrix
        matrix.append(current_row)

    return matrix
