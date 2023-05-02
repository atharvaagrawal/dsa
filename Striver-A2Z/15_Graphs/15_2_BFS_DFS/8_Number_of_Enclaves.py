""" 
https://leetcode.com/problems/number-of-enclaves/description/

You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.


Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.
"""

from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        # We can use same concept as Surrounded Regions

        row = len(grid)
        col = len(grid[0])

        def dfs(i, j):
            if i >= row or i < 0 or j >= col or j < 0:
                return

            if grid[i][j] == 0 or grid[i][j] == 2:
                return

            # Make '1' to '2'
            grid[i][j] = 2

            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        # Traversing through the boundary
        for i in range(row):
            for j in range(col):
                if i == 0 or j == 0 or i == row-1 or j == col-1 and grid[i][j] == 1:
                    dfs(i, j)

        c = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    c += 1

        return c
