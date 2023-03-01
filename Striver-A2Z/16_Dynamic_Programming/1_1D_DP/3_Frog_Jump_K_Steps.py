""" 
There are n stones and an array of heights and Geek is standing at stone 1 and can jump to 
one of the following: Stone i+1, i+2, ... i+k stone and cost will be [hi-hj] is incurred, 
where j is the stone to land on. Find the minimum possible total cost incurred before the 
Geek reaches Stone N.

Example 1:
Input:
n = 5, k = 3
heights = {10, 30, 40, 50, 20}
Output:
30
Explanation:
Geek will follow the path 1->2->5, the total cost 
would be | 10-30| + |30-20| = 30, which is minimum
"""

# Tabulation
class Solution:
    def minimizeCost(self, height, n, k):
        
        dp = [-1]*n
        dp[0] = 0
        
        for i in range(1,n):
            m = float('inf')
        
            for j in range(1,k+1):
                if i-j >= 0:
                    cost = dp[i-j] + abs(height[i]-height[i-j])
                    m = min(cost,m)
            
            dp[i] = m
        
        return dp[n-1]

""" 
# Using Recursion
class Solution:
    def minimizeCost(self, height, n, k):      
          
        def minE(height,n,k):
            if n == 0:
                return 0
            
            m = float('inf')
            
            for i in range(1,k+1):
                if n-i >= 0:
                    cost = minE(height,n-i,k) + abs(height[n] - height[n-i])
                    m = min(m,cost)
                    
            return m
        
        return minE(height,n-1,k)
 """
""" 
# Using Memorization

class Solution:
    def minimizeCost(self, height, n, k):
        
        dp = [-1]*n
  
        
        def minE(height,n,k):
            if n == 0:
                return 0
            
            m = float('inf')
            
            if dp[n] != -1:
                return dp[n]
            
            for i in range(1,k+1):
                if n-i >= 0:
                    cost = minE(height,n-i,k) + abs(height[n] - height[n-i])
                    m = min(m,cost)
                    
            dp[n] = m
            return dp[n]
        
        return minE(height,n-1,k) 
"""