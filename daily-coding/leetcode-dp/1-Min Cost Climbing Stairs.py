""" 
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, 
you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor. 

Example 1:
Input: cost = [10,15,20]
Output: 15

Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6

Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
"""
from typing import List

""" 
# Recursion TLE
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def find(cost,n):
            if n == 0:
                return cost[n]
            
            pick1 = cost[n]
            if n > 1:
                pick1 = cost[n] + find(cost,n-2)
            pick2 = cost[n] + find(cost,n-1)
            
            print(n,pick1,pick2)

            return min(pick1,pick2)

        n = len(cost)        
        return min(find(cost,n-1),find(cost,n-2))
"""
# Memorization Accepted
""" class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def find(cost,n):
            if n == 0:
                return cost[n]

            if dp[n] != -1:
                return dp[n]

            pick1 = cost[n]
            if n > 1:
                pick1 = cost[n] + find(cost,n-2)
            pick2 = cost[n] + find(cost,n-1)

            # print(n,pick1,pick2)

            dp[n] = min(pick1,pick2)

            return dp[n]

        n = len(cost)
        dp = [-1]*n
        res1 = find(cost,n-1)
        dp = [-1]*n
        res2 = find(cost,n-2)        

        return min(res1,res2)
 """

# Tabulation
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def find(cost,n):
            dp = [-1]*(n+1)
            dp[0] = cost[0]
            print(cost,n)
            for i in range(1,n+1):
                pick1 = cost[i]
                if i > 1:
                    pick1 = cost[i] + dp[i-2]
                pick2 = cost[i] + dp[i-1]

                dp[i] = min(pick1,pick2)          
            return min(dp[n],dp[n-1])

        n = len(cost)
        res1 = find(cost,n-1)
        
        return res1

obj = Solution()
cost = [1,100,1,1,1,100,1,1,100,1]
# cost = [10,15,20]
print(obj.minCostClimbingStairs(cost))
