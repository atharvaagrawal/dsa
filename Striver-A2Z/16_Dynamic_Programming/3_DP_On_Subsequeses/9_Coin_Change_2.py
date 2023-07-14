# https://leetcode.com/problems/coin-change-ii/description/
""" 
You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money 
cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.


Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:

Input: amount = 10, coins = [10]
Output: 1
"""

from typing import List


# Memoization
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [[-1 for i in range(amount+1)] for _ in range(len(coins))]

        def solve(ind, target):
            if target == 0:
                return 1
            if ind < 0:
                return 0

            if dp[ind][target] != -1:
                return dp[ind][target]

            take = notTake = 0

            if coins[ind] <= target:
                take = solve(ind, target-coins[ind])
            notTake = solve(ind-1, target)

            dp[ind][target] = take+notTake

            return take+notTake

        return solve(len(coins)-1, amount)


# Tabulation
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [[0 for i in range(amount+1)] for _ in range(len(coins))]

        # Base Condition
        for i in range(amount+1):
            if i % coins[0] == 0:
                dp[0][i] = 1

        for ind in range(1, len(coins)):
            for target in range(0, amount+1):
                notTake = dp[ind-1][target]

                take = 0
                if coins[ind] <= target:
                    take = dp[ind][target-coins[ind]]

                dp[ind][target] = notTake+take

        return dp[len(coins)-1][amount]
