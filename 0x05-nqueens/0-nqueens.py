#!/usr/bin/python3
import sys


def is_position_safe(placed_queens, new_row, new_col):
    """Check if a new queen can be safely placed at given row and column."""
    for row, col in placed_queens:
        if col == new_col or abs(row - new_row) == abs(col - new_col):
            return False
    return True


def find_nqueens_solutions(board_size):
    """Solve the N Queens problem using backtracking."""
    def place_queens(row=0, queens_positions=[]):
        if row == board_size:
            all_solutions.append(queens_positions[:])
            return
        for col in range(board_size):
            if is_position_safe(queens_positions, row, col):
                queens_positions.append([row, col])
                place_queens(row + 1, queens_positions)
                queens_positions.pop()

    all_solutions = []
    place_queens()
    return all_solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = find_nqueens_solutions(board_size)
    for solution in solutions:
        print(solution)
