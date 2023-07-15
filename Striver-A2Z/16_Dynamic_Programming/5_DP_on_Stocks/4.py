# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/
""" 
You are given an integer array prices where prices[i] is the price 
of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions: i.e. 
you may buy at most k times and sell at most k times.

Note: You may not engage in multiple transactions simultaneously 
(i.e., you must sell the stock before you buy again).
 

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. 
Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""

from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        # At Most 2 Transcation's
        n = len(prices)

        dp = [[[-1 for _ in range(k+1)] for _ in range(2)] for _ in range(n)]

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

        return solve(0, 1, k)
