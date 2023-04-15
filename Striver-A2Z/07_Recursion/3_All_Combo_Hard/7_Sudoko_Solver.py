# https://leetcode.com/problems/sudoku-solver/description/
""" 
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.
"""

from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def isValid(row, col, c):
            # Check Row and Col
            for i in range(9):
                if board[row][i] == c:
                    return False
                if board[i][col] == c:
                    return False

                # Check the 3x3
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c:
                    return False
            return True

        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for c in "123456789":
                            if isValid(i, j, c):
                                board[i][j] = c
                                if solve():
                                    return True
                                else:
                                    board[i][j] = "."
                        return False
            return True
        return solve()
