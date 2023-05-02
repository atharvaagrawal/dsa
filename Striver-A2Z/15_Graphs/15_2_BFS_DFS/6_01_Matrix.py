""" 
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1. 

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""

from typing import List
from queue import Queue
import copy


# BFS
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = Queue()

        row = len(mat)
        col = len(mat[0])

        visited = [[0 for _ in range(col)] for _ in range(row)]
        distance = copy.deepcopy(visited)

        # Take 0 with distance 0
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    visited[i][j] = 1
                    queue.put([i, j, 0])

        # Traverse in 4 direction
        direction_x = [-1, 0, 1, 0]
        direction_y = [0, 1, 0, -1]

        while queue.qsize():
            n = queue.qsize()

            for _ in range(n):
                i, j, steps = queue.get()

                distance[i][j] = steps

                # print(i,j,steps)

                # Check the 4 direction
                for neig in range(4):
                    nrow = i + direction_x[neig]
                    ncol = j + direction_y[neig]

                    # print(nrow, ncol)
                    if nrow >= 0 and nrow < row and ncol >= 0 and ncol < col and visited[nrow][ncol] == 0:
                        visited[nrow][ncol] = 1
                        queue.put([nrow, ncol, steps+1])

        return distance


# DFS: TLE
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        # We need to find the distance of the 0
        row = len(mat)
        col = len(mat[0])

        # print(mat)

        def dfs(i, j):
            # print(i,j)
            # Base Case
            if i >= row or i < 0 or j >= col or j < 0 or visited[i][j]:
                return float("inf")

            if mat[i][j] == 0:
                # print('in',i,j)
                return 0
            visited[i][j] = 1

            c1 = dfs(i-1, j)
            # print('c1',c1)
            c2 = dfs(i+1, j)
            # print('with c2',c2)

            c3 = dfs(i, j-1)
            # print('c3:',c3)
            c4 = dfs(i, j+1)
            # print('oo',c4)

            visited[i][j] = 0

            return min(c1, c2, c3, c4) + 1

        visited = [[0 for i in range(col)] for j in range(row)]
        print(visited)

        res = []
        for i in range(row):
            tmp = []
            for j in range(col):
                if mat[i][j] == 0:
                    tmp.append(0)
                else:
                    # print(i,j,mat[i][j])
                    tmp.append(dfs(i, j))
            res.append(tmp)
            # print(res)

        return res
