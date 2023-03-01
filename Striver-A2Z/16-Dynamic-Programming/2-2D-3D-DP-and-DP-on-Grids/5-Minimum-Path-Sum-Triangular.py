""" 
https://leetcode.com/problems/triangle/

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, 
if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
Input: triangle = [[-10]]
Output: -10
"""
from typing import List 

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        # i,j row,col
        
        dp = []
        for j in range(n):
            l = []
            for i in range(len(triangle[j])):
                l.append(-1)
            dp.append(l)

        def minTriangle(i,j):
            if i == n-1:
                return triangle[i][j]

            if dp[i][j] != -1:
                return dp[i][j]

            down = triangle[i][j] + minTriangle(i+1,j)
            diagonal = triangle[i][j] + minTriangle(i+1,j+1)
            
            dp[i][j] = min(down,diagonal)
            
            return dp[i][j]

        print(minTriangle(0,0))

obj = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle = [[-10]]
triangle = [[2],[3,60],[60,5,60],[50,60,60,3]]
obj.minimumTotal(triangle)