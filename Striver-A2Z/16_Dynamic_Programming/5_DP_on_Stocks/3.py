# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/


""" 
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.


Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. 
You must sell before buying again.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # At Most 2 Transcation's
        n = len(prices)

        # 1 - buy 0 - sell
        def solve(ind, buy, trans):
            if ind == n:
                return 0

            if trans == 2:
                return 0

            profit = 0

            if buy:
                profit = max(-prices[ind]+solve(ind+1, 0,
                             trans), 0+solve(ind+1, 1, trans))
            else:
                profit = max(prices[ind]+solve(ind+1, 1,
                             trans+1), 0+solve(ind+1, 0, trans))

            return profit

        return solve(0, 1, 0)


# Memoization
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # At Most 2 Transcation's
        n = len(prices)

        dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]

        # 1 - buy 0 - sell
        def solve(ind, buy, trans):
            if ind == n or trans == 0:
                return 0

            if dp[ind][buy][trans] != -1:
                return dp[ind][buy][trans]

            profit = 0

            if buy:
                profit = max(-prices[ind]+solve(ind+1, 0,
                             trans), 0+solve(ind+1, 1, trans))
            else:
                profit = max(prices[ind]+solve(ind+1, 1,
                             trans-1), 0+solve(ind+1, 0, trans))

            dp[ind][buy][trans] = profit

            return profit

        return solve(0, 1, 2)


# Tabulation
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # At Most 2 Transcation's
        n = len(prices)

        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n+1)]

        for ind in range(n-1, -1, -1):
            for buy in range(2):
                for trans in range(1, 3):
                    profit = 0

                    if buy:
                        profit = max(-prices[ind]+dp[ind+1]
                                     [0][trans], 0+dp[ind+1][1][trans])
                    else:
                        profit = max(prices[ind]+dp[ind+1][1]
                                     [trans-1], 0+dp[ind+1][0][trans])

                    dp[ind][buy][trans] = profit

        return dp[0][1][2]


# Space Optimization
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # At Most 2 Transcation's
        n = len(prices)

        # trans , buy
        ahead = [[0 for _ in range(3)] for _ in range(2)]
        curr = [[0 for _ in range(3)] for _ in range(2)]

        for ind in range(n-1, -1, -1):
            for buy in range(2):
                for trans in range(1, 3):
                    profit = 0

                    if buy:
                        curr[buy][trans] = max(-prices[ind] +
                                               ahead[0][trans], 0+ahead[1][trans])
                    else:
                        curr[buy][trans] = max(
                            prices[ind]+ahead[1][trans-1], 0+ahead[0][trans])

            ahead = curr

        return ahead[1][2]
