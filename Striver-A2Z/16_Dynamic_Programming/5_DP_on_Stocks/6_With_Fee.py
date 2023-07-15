# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
""" 
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for 
each transaction.

Note:

You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
The transaction fee is only charged once for each stock purchase and sale.
 
Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Example 2:

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        n = len(prices)

        # 1 - buy
        # 0 - sell
        dp = [[-1 for _ in range(2)] for _ in range(n+1)]

        def solve(ind, buy):
            if ind >= n:
                return 0

            profit = 0

            if dp[ind][buy] != -1:
                return dp[ind][buy]

            if buy:
                profit = max(-prices[ind]+solve(ind+1, 0), 0 + solve(ind+1, 1))
            else:
                profit = max(prices[ind]-fee +
                             solve(ind+1, 1), 0 + solve(ind+1, 0))

            dp[ind][buy] = profit

            return profit

        return solve(0, 1)
