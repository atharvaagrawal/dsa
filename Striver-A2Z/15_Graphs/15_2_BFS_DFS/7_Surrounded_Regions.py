""" 
https://leetcode.com/problems/surrounded-regions/description/

Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped. 
"""

from typing  import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # If on border do not filp it
        row = len(board)
        col = len(board[0])
        
        # In the 4 direction we have to see whether X is there or not
        def dfs(i,j):
            if i >= row or i < 0 or j >= col or j < 0 :
                return 
            
            if board[i][j] == 'X' or board[i][j] == '1':
                return 

            # Making 'O' to '1' 
            board[i][j] = '1'
            dfs(i,j-1) 
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i+1,j) 
            
        # Go to the boundary
        for i in range(row):
            for j in range(col):
                if i == 0 or i == row - 1 or j == 0 or j == col-1 and board[i][j] == 'O':
                    dfs(i,j)
        
        # print(board)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '1':
                    board[i][j] = 'O'

