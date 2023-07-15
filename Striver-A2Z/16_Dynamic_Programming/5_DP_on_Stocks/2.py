# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
""" 
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the 
stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.


Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
"""

from typing import List


# Recurrance
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # 1 - Buy
        # 0 - Sell
        def solve(ind, buy):
            if ind == n:
                return 0

            profit = 0

            if buy:
                # Buy or not buy
                profit = max(-prices[ind]+solve(ind+1, 0), 0+solve(ind+1, 1))
            else:
                # Sell or not sell
                profit = max(prices[ind] + solve(ind+1, 1),
                             0 + solve(ind+1, 0))

            return profit

        return solve(0, 1)


# Memoization
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # 1 - Buy
        # 0 - Sell

        dp = [[-1 for _ in range(n+1)] for _ in range(2)]

        def solve(ind, buy):
            if ind == n:
                return 0

            if dp[buy][ind] != -1:
                return dp[buy][ind]

            profit = 0

            if buy:
                # Buy or not buy
                profit = max(-prices[ind]+solve(ind+1, 0), 0+solve(ind+1, 1))
            else:
                # Sell or not sell
                profit = max(prices[ind] + solve(ind+1, 1),
                             0 + solve(ind+1, 0))

            dp[buy][ind] = profit

            return profit

        return solve(0, 1)


# Tabulation
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # 1 - Buy
        # 0 - Sell

        dp = [[0 for _ in range(2)] for _ in range(n+1)]
        dp[n][0] = dp[n][1] = 0

        for ind in range(n-1, -1, -1):
            for buy in range(2):
                profit = 0

                if buy:
                    # Buy or not buy
                    profit = max(-prices[ind]+dp[ind+1][0], 0+dp[ind+1][1])
                else:
                    # Sell or not sell
                    profit = max(prices[ind] + dp[ind+1][1], 0 + dp[ind+1][0])

                dp[ind][buy] = profit

        return dp[0][1]


# Space Optimization
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # 1 - Buy
        # 0 - Sell
        next_buy = next_sell = 0

        for ind in range(n-1, -1, -1):
            for buy in range(2):
                profit = 0

                if buy:
                    # Buy or not buy
                    profit = max(-prices[ind]+next_sell, 0+next_buy)
                else:
                    # Sell or not sell
                    profit = max(prices[ind] + next_buy, 0 + next_sell)

                if buy == 0:
                    next_sell = profit
                else:
                    next_buy = profit

        return next_buy
