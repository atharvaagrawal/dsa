# https://leetcode.com/problems/longest-increasing-subsequence/
""" 
Given an integer array nums, return the length of the longest strictly increasing  subsequence.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""

# Recurssion

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        def solve(ind, prev):

            if ind == n:
                return 0

            notTake = 0 + solve(ind+1, prev)
            take = float('-inf')
            if nums[ind] > prev:
                take = 1 + solve(ind+1, nums[ind])

            return max(take, notTake)

        return solve(0, float('-inf'))


# Memoization
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [[-1 for i in range(n+1)] for _ in range(n)]

        # for prev coordinate change
        def solve(ind, prev):
            if ind == n:
                return 0

            if dp[ind][prev+1] != -1:
                return dp[ind][prev+1]

            notTake = 0 + solve(ind+1, prev)
            take = float('-inf')

            if prev == -1 or nums[ind] > nums[prev]:
                take = 1 + solve(ind+1, ind)

            dp[ind][prev+1] = max(take, notTake)

            return max(take, notTake)

        return solve(0, -1)
