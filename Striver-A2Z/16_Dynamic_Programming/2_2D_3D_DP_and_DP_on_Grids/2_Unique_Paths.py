""" 
Unique Paths

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either 
down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach 
the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Input: m = 3, n = 2
Output: 3

# m = rows
# n = cols
[[1,2],
 [1,2],
 [1,2]]

Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""

# Recursion TLE
""" m =23
n = 12
class Solution: 
    def uniquePaths(self, m: int, n: int) -> int:
        
        def paths(row,col):
            if row == m-1 and col == n-1:
                return 1

            if row >= m:
                return 0
            if col >= n:
                return 0

            # two moves possible right i.e [m,n+1] and down [m+1,n]            
            count = paths(row,col+1)
            count1 = paths(row+1,col)
            
            return count+count1

        print(paths(0,0))
"""

# Memorization Accepted
class Solution: 
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[-1 for i in range(n)] for j in range(m)]

        def paths(row,col):
            if row == m-1 and col == n-1:
                return 1

            if row >= m:
                return 0
            if col >= n:
                return 0

            if dp[row][col] != -1:
                return dp[row][col]

            # two moves possible right i.e [m,n+1] and down [m+1,n]            
            count = paths(row,col+1)
            count1 = paths(row+1,col)
            
            dp[row][col] = count+count1

            return dp[row][col]

        print(paths(0,0))

# Tabulation Accepted
class Solution: 
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[-1 for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                dp[i][j] = 0 
       

obj = Solution()

m = 3
n = 2
obj.uniquePaths(m,n)


