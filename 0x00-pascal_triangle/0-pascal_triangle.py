#!/usr/bin/python3
def pascal_triangle(n):
    # Return an empty list
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Loop to generate each row from the 2nd row to the nth row
    for i in range(1, n):
        # Get the last row in the current triangle
        prev_row = triangle[-1]
        # Start each new row with a 1
        new_row = [1]

        # Fill in the middle values of the new row
        # Each value is the sum of 2 values above it in the previous row
        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])

        # End the new row with a 1
        new_row.append(1)

        # Add the newly created row to the triangle
        triangle.append(new_row)

    # Return the complete Pascal's Triangle
    return triangle
