# https://practice.geeksforgeeks.org/problems/number-of-distinct-islands/1

""" 
Given a boolean 2D matrix grid of size n * m. You have to find the number of distinct islands where a group of connected 1s 
(horizontally or vertically) forms an island. Two islands are considered to be distinct if and only if one island is not equal 
to another (not rotated or reflected).

Input:
grid[][] = {{1, 1, 0, 0, 0},
            {1, 1, 0, 0, 0},
            {0, 0, 0, 1, 1},
            {0, 0, 0, 1, 1}}
Output:
1


Input:
grid[][] = {{1, 1, 0, 1, 1},
            {1, 0, 0, 0, 0},
            {0, 0, 0, 0, 1},
            {1, 1, 0, 1, 1}}
Output:
3
"""

import sys
from typing import List
sys.setrecursionlimit(10**8)


class Solution:
    def countDistinctIslands(self, grid: List[List[int]]) -> int:
        # Use DFS
        # We can traverse in 4 direction only 1) top 2) left 3) down 4) right

        row = len(grid)
        col = len(grid[0])

        def dfs(i, j, tmp, r, c):
            # Base Case
            if i >= row or i < 0 or j >= col or j < 0:
                return

            if visited[i][j] or grid[i][j] == 0:
                return

            visited[i][j] = 1
            tmp.append((i-r, j-c))

            # Traverse
            # Up
            dfs(i-1, j, tmp, r, c)

            # Left
            dfs(i, j-1, tmp, r, c)

            # Down
            dfs(i+1, j, tmp, r, c)

            # Right
            dfs(i, j+1, tmp, r, c)

        visited = [[0 for _ in range(col)] for _ in range(row)]

        res = set()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    tmp = []
                    dfs(i, j, tmp, i, j)
                    if tmp:
                        res.add(tuple(tmp.copy()))

        return len(res)
