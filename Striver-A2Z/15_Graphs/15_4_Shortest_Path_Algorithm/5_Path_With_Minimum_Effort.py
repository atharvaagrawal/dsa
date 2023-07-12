# https://leetcode.com/problems/path-with-minimum-effort/description/

""" 
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, 
where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, 
(0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can 
move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.


Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, 
which is better than route [1,3,5,3,5].
"""

from queue import PriorityQueue
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        row = len(heights)
        col = len(heights[0])

        distance = [[float('inf') for _ in range(col)] for _ in range(row)]

        distance[0][0] = 0
        q = PriorityQueue()

        # distance row, col
        q.put([0, [0, 0]])

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        while not q.empty():
            dis, r = q.get()

            c = r[1]
            r = r[0]
            if r == row-1 and c == col-1:
                return dis

            for i in range(4):
                newr = r+dr[i]
                newc = c+dc[i]

                if newr >= 0 and newr < row and newc >= 0 and newc < col:
                    diff = max(dis, abs(heights[r][c]-heights[newr][newc]))

                    if diff < distance[newr][newc]:
                        distance[newr][newc] = diff

                        q.put([diff, [newr, newc]])

        return 1
