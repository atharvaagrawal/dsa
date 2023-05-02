""" 
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as 
the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all 
of the aforementioned pixels with color.

Return the modified image after performing the flood fill. 

Example 1:

Input: image = [[1,1,1],
                [1,1,0],
                [1,0,1]], 

sr = 1, sc = 1, color = 2

Output: [[2,2,2],
         [2,2,0],
         [2,0,1]]

Explanation: 
From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), 
all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example 2:
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.

"""

from typing import List
import copy

from queue import Queue


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        row = len(image)
        col = len(image[0])
        visited = copy.deepcopy(image)
        org_col = image[sr][sc]
        same_col = -1

        # if same color
        if org_col == color:
            same_col = org_col
            org_col = -1
            for i in range(row):
                for j in range(col):
                    if visited[i][j] == org_col:
                        visited[i][j] = -1

        def dfs(i, j):
            if i >= row or i < 0 or j >= col or j < 0:
                return

            if visited[i][j] != org_col:
                return

            visited[i][j] = color

            # Check 4-direction
            # UP
            if i >= 1:
                dfs(i-1, j)

            # DOWN
            if i < row-1:
                dfs(i+1, j)

            # LEFT
            if j >= 1:
                dfs(i, j-1)

            # DOWN
            if j < col-1:
                dfs(i, j+1)

        dfs(sr, sc)

        visited[sr][sc] = color
        if same_col != -1:
            for i in range(row):
                for j in range(col):
                    if visited[i][j] == org_col:
                        visited[i][j] = same_col
        return visited
