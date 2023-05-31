# https://leetcode.com/problems/jump-game-ii/description/

""" 
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].


Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

"""

from typing import List

# Simplifies Greedy BFS


class Solution:
    def jump(self, nums: List[int]) -> int:

        res = 0
        l = r = 0

        while r < len(nums)-1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i+nums[i])
            l = r+1
            r = farthest
            res += 1

        return res

# Using DP


class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [-1]*n

        def solve(i, c):
            if i >= n-1:
                dp[-1] = 0
                return c

            if dp[i] != -1:
                return dp[i]+c

            mini = float('inf')

            for pos in range(1, nums[i]+1):
                if pos+i >= n:
                    break

                mini = min(solve(pos+i, 1), mini)

            dp[i] = mini
            return mini + c

        return solve(0, 0)
