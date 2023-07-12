# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

""" 
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.
"""

from queue import PriorityQueue
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        # If source and destination is same
        if grid[0][0] or grid[-1][-1]:
            return -1
        if len(grid) == 1:
            return 1

        row = len(grid)
        col = len(grid[0])

        # Initial-Configuration Distance Matrix
        distance = [[float('inf') for _ in range(col)] for _ in range(row)]

        distance[0][0] = 1

        # Distance Row,Col
        q = [[0, [0, 0]]]

        # 8-Direction to traverse
        dr = [1, -1, 0, 0, 1, 1, -1, -1]
        dc = [0, 0, 1, -1, 1, -1, 1, -1]

        while q:

            dis, r = q.pop(0)

            c = r[1]
            r = r[0]

            # 8 Direction Adjacent Nodes
            for i in range(8):
                newr = r + dr[i]
                newc = c + dc[i]

                if newr >= 0 and newr < row and newc >= 0 and newc < col and grid[newr][newc] == 0 and dis+1 < distance[newr][newc]:
                    distance[newr][newc] = 1+dis
                    q.append([dis+1, [newr, newc]])

                    if newr == row-1 and newc == col-1:
                        return dis+2

        return -1


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        # If source and destination is same
        if grid[0][0] or grid[-1][-1]:
            return -1

        row = len(grid)
        col = len(grid[0])

        # Initial-Configuration Distance Matrix
        distance = [[float('inf')]*col]*row

        distance[0][0] = 1
        q = PriorityQueue()

        # Distance Row,Col
        q.put([1, [0, 0]])

        # 8-Direction to traverse
        dr = [1, -1, 0, 0, 1, 1, -1, -1]
        dc = [0, 0, 1, -1, 1, -1, 1, -1]

        level = 0
        grid[0][0] = 1
        while not q.empty():
            n = q.qsize()
            level += 1

            for _ in range(n):
                dis, r = q.get()

                c = r[1]
                r = r[0]

                if r == row-1 and c == col-1:
                    return level

                # 8 Direction Adjacent Nodes
                for i in range(8):
                    newr = r + dr[i]
                    newc = c + dc[i]

                    if newr >= 0 and newr < row and newc >= 0 and newc < col and grid[newr][newc] == 0:
                        grid[newr][newc] = 1

                        q.put([dis, [newr, newc]])

        return -1
