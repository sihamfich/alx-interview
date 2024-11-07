#!/usr/bin/python3
import sys


def is_safe(queens, row, col):
    for r, c in queens:
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def solve_nqueens(N):
    def backtrack(row=0, queens=[]):
        if row == N:
            solutions.append(queens[:])
            return
        for col in range(N):
            if is_safe(queens, row, col):
                queens.append([row, col])
                backtrack(row + 1, queens)
                queens.pop()

    solutions = []
    backtrack()
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)
