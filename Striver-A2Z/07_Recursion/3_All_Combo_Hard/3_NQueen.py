""" 
https: // leetcode.com/problems/n-queens/

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # No Two Queen Attack
        # If in same row = Attack
        # If in same col = Attack
        # If in same diagonal = Attack

        board = [[0 for i in range(n)] for j in range(n)]

        res = []

        def isSafe(i, j):
            # i = row
            # j = col
            # Check Row and Col
            for r in range(n):
                if board[i][r] == 1:
                    return False
                if board[r][j] == 1:
                    return False

            # Check Diagnoal
            row = i
            col = j

            while row >= 0 and col >= 0:
                if board[row][col] == 1:
                    return False
                row -= 1
                col -= 1

            row = i
            col = j

            while row < n and col >= 0:
                if board[row][col] == 1:
                    return False
                row += 1
                col -= 1

            return True

        def saveres():
            l = []
            for row in board:
                s = ''
                for i in row:
                    if i == 1:
                        s += 'Q'
                    else:
                        s += '.'
                l.append(s)

            res.append(l.copy())

        def solve(col):
            if col == n:
                saveres()
                # print(board)
                return

            for row in range(n):
                if isSafe(row, col):
                    board[row][col] = 1
                    solve(col+1)
                    board[row][col] = 0

        solve(0)

        # print(res)
        return res


obj = Solution()

obj.solveNQueens(4)
