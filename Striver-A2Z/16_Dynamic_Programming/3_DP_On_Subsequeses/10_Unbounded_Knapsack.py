# https://practice.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1
""" 
Given a set of N items, each with a weight and a value, represented by the array w[] and val[] respectively. Also, a knapsack with weight limit W.
The task is to fill the knapsack in such a way that we can get the maximum profit. Return the maximum profit.
Note: Each item can be taken any number of times.

 

Example 1:

Input: N = 2, W = 3
val[] = {1, 1}
wt[] = {2, 1}
Output: 3
Explanation: 
1.Pick the 2nd element thrice.
2.Total profit = 1 + 1 + 1 = 3. Also the total 
  weight = 1 + 1 + 1  = 3 which is <= W.
"""

# Recursion
class Solution:
    def knapSack(self, N, W, val, wt):

        def solve(ind, w):
            if ind == 0:
                return (w//wt[0])*val[0]

            notTake = 0 + solve(ind-1, w)
            take = float('-inf')

            if wt[ind] <= w:
                take = val[ind] + solve(ind, w-wt[ind])

            res = max(take, notTake)

            return res

        return solve(N-1, W)


# Memoization
class Solution:
    def knapSack(self, N, W, val, wt):

        dp = [[-1 for _ in range(W+1)] for _ in range(N)]

        def solve(ind, w):
            if ind == 0:
                return (w//wt[0])*val[0]

            if dp[ind][w] != -1:
                return dp[ind][w]

            notTake = 0 + solve(ind-1, w)
            take = float('-inf')

            if wt[ind] <= w:
                take = val[ind] + solve(ind, w-wt[ind])

            res = max(take, notTake)

            dp[ind][w] = res

            return res

        return solve(N-1, W)


# Tabulation
class Solution:
    def knapSack(self, N, W, val, wt):

        dp = [[0 for _ in range(W+1)] for _ in range(N)]

        for i in range(W+1):
            dp[0][i] = (i//wt[0]) * val[0]

        for ind in range(1, N):
            for w in range(W+1):
                notTake = 0 + dp[ind-1][w]
                take = float('-inf')

                if wt[ind] <= w:
                    take = val[ind] + dp[ind][w-wt[ind]]

                dp[ind][w] = max(take, notTake)

        return dp[N-1][W]
