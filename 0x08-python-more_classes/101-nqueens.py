#!/usr/bin/python3

import sys


def is_safe(board, row, col, N):
    for i in range(col):
        if board[i] == row or board[i] + i == row + col or board[i] - i == col - row:
            return False
    return True


def solve_nqueens(N):
    def backtrack(col):
        if col == N:
            solutions.append(list(board))
            return
        for row in range(N):
            if is_safe(board, row, col, N):
                board[col] = row
                backtrack(col + 1)

    board = [-1] * N
    solutions = []
    backtrack(0)
    return solutions


def print_solutions(solutions):
    for solution in solutions:
        board = [['.' for _ in range(len(solution))] for _ in range(len(solution))]
        for col, row in enumerate(solution):
            board[row][col] = 'Q'
        for row in board:
            print([board.index(row), row.index('Q')])
        print()


def main():
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
    print_solutions(solutions)


if __name__ == '__main__':
    main()

