""" 
https://leetcode.com/problems/rotting-oranges/description/

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally. 

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
"""

from typing import List
import copy
from queue import Queue


# Using BFS
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = Queue()

        row = len(grid)
        col = len(grid[0])

        # First Putting all the Rotten Oranges
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.put([i, j, 0])

        time = 0

        # Now till the queue empty check
        visited = copy.deepcopy(grid)

        while queue.qsize():
            i, j, t = queue.get()

            # Now Check its up, down, left, right
            # UP
            if i >= 1:
                if visited[i-1][j] == 1:
                    visited[i-1][j] = 2
                    queue.put([i-1, j, t+1])
            # DOWN
            if i < row-1:
                if visited[i+1][j] == 1:
                    visited[i+1][j] = 2
                    queue.put([i+1, j, t+1])
            # LEFT
            if j >= 1:
                if visited[i][j-1] == 1:
                    visited[i][j-1] = 2
                    queue.put([i, j-1, t+1])
            # RIGHT
            if j < col-1:
                if visited[i][j+1] == 1:
                    visited[i][j+1] = 2
                    queue.put([i, j+1, t+1])
            time = t

        # Check if any fresh orange left
        for i in range(row):
            for j in range(col):
                if visited[i][j] == 1:
                    return -1
        return time


# Using DP
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # Check if any fresh orange
        def freshOrange(grid):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        return True
            return False

        dp = grid
        minitues = 0

        row = len(grid)
        col = len(grid[0])

        while freshOrange(grid):

            tmp = copy.deepcopy(grid)

            for i in range(row):
                for j in range(col):
                    if grid[i][j] == 2:
                        # Check for up, left, up, down
                        # i = row
                        # j = col

                        # UP
                        if i >= 1:
                            if tmp[i-1][j] == 1:
                                tmp[i-1][j] = 2

                        # DOWN
                        if i < row-1:
                            if tmp[i+1][j] == 1:
                                tmp[i+1][j] = 2

                        # LEFT
                        if j >= 1:
                            if tmp[i][j-1] == 1:
                                tmp[i][j-1] = 2

                        # RIGHT
                        if j < col-1:
                            if tmp[i][j+1] == 1:
                                tmp[i][j+1] = 2

            if tmp == grid:
                return -1

            grid = tmp
            minitues += 1

        return minitues
