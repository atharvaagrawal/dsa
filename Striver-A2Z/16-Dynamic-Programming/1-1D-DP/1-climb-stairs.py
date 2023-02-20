""" 
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2

Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3

Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
""" 
Using Recursion: TLE
class Solution:
    def climbStairs(self, n: int) -> int:

        def climb(c):
            # print(c)
            if c==n:
                return 1
            if c > n:
                return 0

            count = climb(c+1)
            count += climb(c+2)
            
            return count

        return climb(0) 
"""
""" 
Using Memorization: TLE

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1 for i in range(n+1)]
        
        def climb(c):
            # print(c,dp)
            if c==n:
                return 1
            if c > n:
                return 0
            
            if dp[n] != -1:
                return dp[n] 

            left = climb(c+1)
            right = climb(c+2)
            
            dp[c] = left+right

            return dp[c]

        return climb(0)
 """

# Tabulation  
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1 for i in range(n+1)]
        
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

