#!/usr/bin/python3
"""
Defines a function to calculate
the perimeter of an island in a 2D grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in the given 2D grid.

    Args:
        grid (list of list of int): A 2D grid
        where 0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:  # If current cell is land
                perimeter += 4  # Start with 4 sides

                # Check the cell above (if it exists)
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
                    # Remove the common edge with the upper cell

                # Check the cell to the left (if it exists)
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # Remove the common edge with the left cell

    return perimeter
