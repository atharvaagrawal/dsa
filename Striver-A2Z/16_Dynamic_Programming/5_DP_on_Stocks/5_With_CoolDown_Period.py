# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

from typing import List


# Recurrsion
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # 1 - buy
        # 0 - sell

        def solve(ind, buy):
            if ind >= n:
                return 0

            profit = 0

            if buy:
                profit = max(-prices[ind]+solve(ind+1, 0), 0 + solve(ind+1, 1))
            else:
                profit = max(prices[ind]+solve(ind+2, 1), 0 + solve(ind+1, 0))
                # Once sell just skip a day

            return profit

        return solve(0, 1)


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
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
                profit = max(prices[ind]+solve(ind+2, 1), 0 + solve(ind+1, 0))
                # Once sell just skip a day

            dp[ind][buy] = profit

            return profit

        return solve(0, 1)
