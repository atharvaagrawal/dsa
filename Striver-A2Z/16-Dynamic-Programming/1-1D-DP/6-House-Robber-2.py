""" 
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3
"""
from typing import List

# Using Memorization
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        def find(nums,n):
            if n == 0:
                return nums[0]
            
            if n < 0:
                return 0

            if dp[n] != -1:
                return dp[n]

            pick = nums[n] + find(nums,n-2)
            not_pick = 0 + find(nums,n-1)

            dp[n] = max(pick,not_pick)

            return dp[n]
            
        dp = [-1] * n     
        res1 = find(nums[1:],n-2)
        
        dp = [-1] * n 
        res2 = find(nums[:-1],n-2)

        return max(res1,res2)

# Using Tabulation
class Solution:
    def rob(self,nums):
        if len(nums) == 1:
            return nums[0]
            
        def find(nums,n):
            dp = [-1] *(n+1) 

            dp[0] = nums[0]
            # print('he')
            for i in range(1,n+1):
                pick = nums[i]
                if i > 1:
                    pick = nums[i] + dp[i-2]
    
                not_pick = 0 + dp[i-1]

                dp[i] = max(pick,not_pick)

            # print(dp)
            return dp[n]

        n = len(nums)
        return max(find(nums[:-1],n-2),find(nums[1:],n-2))

# Space Optimization
class Solution:
    def rob(self,nums):
        if len(nums) == 1:
            return nums[0]
            
        def find(nums,n):

            prev = nums[0]
            prev2 = 0
            for i in range(1,n+1):
                pick = nums[i]
                if i > 1:
                    pick = nums[i] + prev2
                not_pick = 0 + prev
                
                curr = max(pick,not_pick)

                prev2 = prev 
                prev = curr                
            return prev

        n = len(nums)
        return max(find(nums[:-1],n-2),find(nums[1:],n-2))




