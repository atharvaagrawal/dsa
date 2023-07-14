# https://leetcode.com/problems/coin-change/

""" 
You are given an integer array coins representing coins of different denominations and an 
integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of 
money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
 
Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0
"""
from typing import List


# Recursion: TLE
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def solve(ind, amount):
            if ind == 0:
                if amount % coins[0] == 0:
                    return amount//coins[0]
                else:
                    return float('inf')

            notTake = 0 + solve(ind-1, amount)

            take = float('inf')

            if coins[ind] <= amount:
                take = 1 + solve(ind, amount-coins[ind])

            return min(notTake, take)

        res = solve(len(coins)-1, amount)

        if res == float('inf'):
            return -1

        return res


# DP - Memoization
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [[-1 for i in range(amount+1)] for _ in range(len(coins))]

        def solve(ind, amount):
            if ind == 0:
                if amount % coins[0] == 0:
                    return amount//coins[0]
                else:
                    return float('inf')

            if dp[ind][amount] != -1:
                return dp[ind][amount]

            notTake = 0 + solve(ind-1, amount)

            take = float('inf')

            if coins[ind] <= amount:
                take = 1 + solve(ind, amount-coins[ind])

            dp[ind][amount] = min(notTake, take)

            return dp[ind][amount]

        res = solve(len(coins)-1, amount)

        if res == float('inf'):
            return -1
        return res


# Tabulation
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [[0 for i in range(amount+1)] for _ in range(len(coins))]

        for i in range(amount+1):
            if i % coins[0] == 0:
                dp[0][i] = i//coins[0]
            else:
                dp[0][i] = float('inf')

        for i in range(1, len(coins)):
            for target in range(0, amount+1):
                notTake = 0 + dp[i-1][target]
                take = float('inf')

                if coins[i] <= target:
                    take = 1 + dp[i][target - coins[i]]

                dp[i][target] = min(take, notTake)

        res = dp[len(coins)-1][amount]

        if res == float('inf'):
            return -1
        return res
