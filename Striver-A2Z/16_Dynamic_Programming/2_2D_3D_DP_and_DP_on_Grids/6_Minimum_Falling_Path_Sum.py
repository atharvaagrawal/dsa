""" 
https://leetcode.com/problems/minimum-falling-path-sum/

Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is 
either directly below or diagonally left/right. Specifically, the next element from position (row, col) 
will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1). 

Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.


Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.
"""

from typing import List
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        dp = [[-1 for i in range(n)] for j in range(n)]

        def minPath(i,j):
            if i == n:
                return 0
            if j >= n or j < 0:
                return int(1e9)

            if dp[i][j] != -1:
                return dp[i][j]

            left = matrix[i][j] + minPath(i+1,j-1)
            below = matrix[i][j] + minPath(i+1,j)
            right = matrix[i][j] + minPath(i+1,j+1)

            dp[i][j] = min(left,below,right)
            
            return dp[i][j]
        
        mini = float('inf')
        for col_num in range(n):
            ans = minPath(0,col_num)
            mini = min(mini,ans)

        return mini      

obj = Solution()            

matrix = [[2,1,3],[6,5,4],[7,8,9]]
# matrix = [[-19,57],[-40,-5]]

obj.minFallingPathSum(matrix)