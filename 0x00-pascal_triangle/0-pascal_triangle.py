#!/usr/bin/python3
def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    triangle = []

    # Only proceed if n is greater than 0
    if n > 0:
        for row_num in range(1, n + 1):
            current_row = []
            value = 1

            # Generate the values for the current row
            for position in range(1, row_num + 1):
                current_row.append(value)
                value = value * (row_num - position) // position

            triangle.append(current_row)

    return triangle
