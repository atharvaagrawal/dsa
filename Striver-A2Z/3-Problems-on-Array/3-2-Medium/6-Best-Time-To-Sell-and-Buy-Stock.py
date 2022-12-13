# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(self, prices: List[int])-> int:
        minimum = prices[0]
        max_profit = 0

        for i in prices:  
           minimum = min(minimum,i)
           max_profit = max(max_profit,i-minimum)
        return max_profit
        