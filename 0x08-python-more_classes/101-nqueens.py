#!/usr/bin/python3
"""
Define N queens
"""
import sys

def print_solutions(solutions):
    """Print the list of solutions."""
    for solution in solutions:
        print(solution)

def is_not_under_attack(row, col, queens):
    """Check if the position is safe from attacks by other queens."""
    for r, c in queens:
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True

def backtrack(n, row, queens, solutions):
    """Use backtracking to find all solutions."""
    if row == n:
        solutions.append(queens.copy())
        return
    for col in range(n):
        if is_not_under_attack(row, col, queens):
            queens.append((row, col))
            backtrack(n, row + 1, queens, solutions)
            queens.pop()

def nqueens(n):
    """Find all solutions to the N Queens problem."""
    solutions = []
    backtrack(n, 0, [], solutions)
    return solutions

def main():
    """Main function to handle input and output."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = nqueens(n)
    print_solutions(solutions)

if __name__ == "__main__":
    main()
