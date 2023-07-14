# https://leetcode.com/problems/target-sum/description/
""" 
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:

Input: nums = [1], target = 1
Output: 1
"""

from typing import List


class Solution:
    def countPartitions(self, n, d, arr):
        totalSum = sum(arr)

        s1 = totalSum - d

        if s1 < 0:
            return 0

        if (totalSum-d) % 2 == 1:
            return 0

        s2 = (totalSum-d) // 2

        dp = [[-1 for i in range(s2+1)] for j in range(n+1)]

        # Subset partition difference
        def solve(ind, target):

            if ind == 0:
                if target == 0 and arr[0] == 0:
                    return 2
                if target == 0 or target == arr[0]:
                    return 1
                return 0

            if dp[ind][target] != -1:
                return dp[ind][target]

            take = 0
            notTake = 0

            # Take or Not Take
            if arr[ind] <= target:
                take = solve(ind-1, target-arr[ind])
            notTake = solve(ind-1, target)

            dp[ind][target] = (take + notTake) % (10**9+7)

            return dp[ind][target]

        return solve(n-1, s2)

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        return self.countPartitions(len(nums), target, nums)


# Recurssion
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def solve(ind, target):
            if ind == -1:
                if target == 0:
                    return 1
                return 0

            # Positive Sign or Negative Sign
            pos = solve(ind-1, target+nums[ind])
            neg = solve(ind-1, target-nums[ind])

            return pos+neg

        return solve(n-1, target)


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}

        def solve(ind, currSum):
            if ind < 0 and currSum == target:
                return 1
            if ind < 0:
                return 0

            if (ind, currSum) in dp:
                return dp[(ind, currSum)]

            # Positive Sign or Negative Sign
            pos = solve(ind-1, currSum+nums[ind])
            neg = solve(ind-1, currSum-nums[ind])

            dp[(ind, currSum)] = pos+neg

            return pos+neg

        return solve(n-1, 0)
