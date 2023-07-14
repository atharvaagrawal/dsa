# https://practice.geeksforgeeks.org/problems/rod-cutting0840/1
""" 
Given a rod of length N inches and an array of prices, price[]. price[i] denotes the value of a 
piece of length i. Determine the maximum value obtainable by cutting up the rod and selling the pieces.

Note: Consider 1-based indexing.

Example 1:

Input:
N = 8
Price[] = {1, 5, 8, 9, 10, 17, 17, 20}
Output:
22
Explanation:
The maximum obtainable value is 22 by 
cutting in two pieces of lengths 2 and 
6, i.e., 5+17=22.

Example 2:

Input:
N=8
Price[] = {3, 5, 8, 9, 10, 17, 17, 20}
Output: 
24
Explanation: 
The maximum obtainable value is 
24 by cutting the rod into 8 pieces 
of length 3, i.e, 8*3=24. 
"""


# Recursion
class Solution:
    def cutRod(self, price, n):

        # N - length of rod Inches
        # price[N] - the value of a piece of length i

        def solve(ind, n):
            if ind == 0:
                return n*price[ind]

            notTake = 0 + solve(ind-1, n)

            take = float('-inf')

            if ind+1 <= n:
                take = price[ind] + solve(ind, n-(ind+1))

            return max(take, notTake)

        return solve(n-1, n)


# Memoization
class Solution:
    def cutRod(self, price, n):

        # N - length of rod Inches
        # price[N] - the value of a piece of length i

        dp = [[-1 for _ in range(n+1)] for _ in range(n)]

        def solve(ind, n):
            if ind == 0:
                return n*price[ind]

            if dp[ind][n] != -1:
                return dp[ind][n]

            notTake = 0 + solve(ind-1, n)

            take = float('-inf')

            if ind+1 <= n:
                take = price[ind] + solve(ind, n-(ind+1))

            dp[ind][n] = max(take, notTake)

            return dp[ind][n]

        return solve(n-1, n)


class Solution:
    def cutRod(self, price, n):

        # N - length of rod Inches
        # price[N] - the value of a piece of length i

        dp = [[-1 for _ in range(n+1)] for _ in range(n)]

        for i in range(n+1):
            dp[0][i] = i*price[0]

        for ind in range(1, n):
            for rod in range(n+1):

                notTake = 0 + dp[ind-1][rod]

                take = float('-inf')

                if ind+1 <= rod:
                    take = price[ind] + dp[ind][rod-(ind+1)]

                dp[ind][rod] = max(take, notTake)

        return dp[n-1][n]
