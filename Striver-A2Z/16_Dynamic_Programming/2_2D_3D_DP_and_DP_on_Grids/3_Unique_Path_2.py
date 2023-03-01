""" 

You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either 
down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot 
include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.


Input: obstacleGrid = 
    [[0,0,0],
     [0,1,0],
     [0,0,0]]

Output: 2 
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right


Input: obstacleGrid = 
        [[0,1],
         [0,0]]
Output: 1

"""

from typing import List

""" 
# Recursion 
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[m-1][n-1] == 1:
            return 0

        def paths(row,col):
            if row == m-1 and col == n-1:
                return 1

            if row >= m:
                return 0
            if col >= n:
                return 0

            if obstacleGrid[row][col] == 1:
                return 0

            # two moves possible right i.e [m,n+1] and down [m+1,n]            
            count = paths(row,col+1)
            count1 = paths(row+1,col)
            
            return count+count1

        print(paths(0,0))
"""

# Memorization
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [[-1 for i in range(n)] for j in range(m)]
        
        if obstacleGrid[m-1][n-1] == 1:
            return 0

        def paths(row,col):
            if row == m-1 and col == n-1:
                return 1

            if row >= m:
                return 0
            if col >= n:
                return 0

            if obstacleGrid[row][col] == 1:
                return 0

            if dp[row][col] != -1:
                return dp[row][col]
            
            # two moves possible right i.e [m,n+1] and down [m+1,n]            
            count = paths(row,col+1)
            count1 = paths(row+1,col)
            
            dp[row][col] =  count+count1
            
            return dp[row][col]
        print(paths(0,0))

obj = Solution()

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
obstacleGrid = [[0,0],
                [0,1]]  # Expected Ans = 0

obj.uniquePathsWithObstacles(obstacleGrid)