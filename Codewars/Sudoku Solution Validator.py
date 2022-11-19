"""
Sudoku Background
Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
(More info at: http://en.wikipedia.org/wiki/Sudoku)

Sudoku Solution Validator
Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.

Examples
validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]); // => true
validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 0, 3, 4, 8],
  [1, 0, 0, 3, 4, 2, 5, 6, 0],
  [8, 5, 9, 7, 6, 1, 0, 2, 0],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 0, 1, 5, 3, 7, 2, 1, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 0, 0, 4, 8, 1, 1, 7, 9]
]); // => false
"""


def valid_solution(board):
    if check_lines(board) and check_arrays(board) and check_squares(board):
        return True
    return False


def check_square(board, a, b):
    s = (board[a][b:b + 3] + board[a + 1][b:b + 3] + board[a + 2][b:b + 3])
    s.sort()
    if s == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return True
    return False


def check_lines(board):
    for i in range(len(board)):
        l = board[i][:]
        l.sort()
        if l != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    return True


def check_arrays(board):
    board = [[r[col] for r in board] for col in range(len(board[0]))]
    return check_lines(board)


def check_squares(board):
    if check_square(board, 0, 0) and check_square(board, 0, 3) and check_square(board, 0, 6) and check_square(board, 3,
                                                                                                              0) and check_square(
            board, 3, 3) and check_square(board, 3, 6) and check_square(board, 6, 0) and check_square(board, 6,
                                                                                                      3) and check_square(
            board, 6, 6):
        return True
    return False