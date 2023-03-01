""" 
https://leetcode.com/problems/minimum-path-sum/

Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],
               [1,5,1],
               [4,2,1]]
Output: 7

Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""

from typing import List
""" 
Recursion
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        def allWays(row,col):    
            if row == 0 and col == 0:
                return grid[row][col]
            
            if row < 0:
                return int(1e9)
            if col < 0:
                return int(1e9)
            
            # down or right
            down = grid[row][col] + allWays(row-1,col) 
            right = grid[row][col] + allWays(row,col-1)

            print(down,right,row,col)
            return min(down,right)        

        print(allWays(m-1,n-1))
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for i in range(n)] for j in range(m)]

        def allWays(row,col):    
            if row == 0 and col == 0:
                return grid[row][col]
            
            if row < 0:
                return int(1e9)
            if col < 0:
                return int(1e9)
            
            if dp[row][col] != -1:
                return dp[row][col]

            # down or right
            down = grid[row][col] + allWays(row-1,col) 
            right = grid[row][col] + allWays(row,col-1)

            # print(down,right,row,col)
            dp[row][col] =  min(down,right)        
            return dp[row][col]

        return allWays(m-1,n-1)

obj = Solution()
grid = [[1,3,1],
        [1,5,1],
        [4,2,1]]

obj.minPathSum(grid)