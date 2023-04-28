""" 
https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/

Partition Array Into Two Arrays to Minimize Sum Difference
You are given an integer array nums of 2 * n integers. You need to partition nums into two arrays of length n 
to minimize the absolute difference of the sums of the arrays. To partition nums, put each element of nums into 
one of the two arrays.

Return the minimum possible absolute difference.


Example 1:
Input: nums = [3,9,7,3]
Output: 2
Explanation: One optimal partition is: [3,9] and [7,3].
The absolute difference between the sums of the arrays is abs((3 + 9) - (7 + 3)) = 2.

Example 2:
Input: nums = [-36,36]
Output: 72
Explanation: One optimal partition is: [-36] and [36].
The absolute difference between the sums of the arrays is abs((-36) - (36)) = 72.

Example 3:
Input: nums = [2,-1,0,4,-2,-9]
Output: 0
Explanation: One optimal partition is: [2,4,-9] and [-1,0,-2].
The absolute difference between the sums of the arrays is abs((2 + 4 + -9) - (-1 + 0 + -2)) = 0.
"""
from typing import List


# Memoization
class Solution:
    def minDifference(self, arr, n):
        totalSum = sum(arr)

        if n == 1:
            return arr[0]

        dp = [[-1 for i in range(totalSum+1)] for j in range(n+1)]

        # Subset partition difference

        def solve(ind, target):
            if target == 0:
                return True
            if ind == 0:
                return arr[0] == target

            if dp[ind][target] != -1:
                return dp[ind][target]

            take = False
            notTake = False

            # Take or Not Take
            if arr[ind] <= target:
                take = solve(ind-1, target-arr[ind])
            notTake = solve(ind-1, target)

            dp[ind][target] = take or notTake

            return dp[ind][target]

        # Creating n-1 dp of all value
        for i in range(totalSum+1):
            solve(n-1, i)

        mine = float('inf')

        for i in range(totalSum+1):
            if dp[n-1][i]:
                diff = abs(i - (totalSum-i))
                mine = min(mine, diff)

        return mine % (10**9 + 7)


# Not For Negative Numbers
# Tabulation
# class Solution:
#     def minimumDifference(self, nums: List[int]) -> int:

#         totalSum = sum(nums)
#         k = totalSum

#         # print(totalSum)

#         dp = [[False for i in range(k+1)] for i in range(len(nums))]
#         # print(dp)

#         # SubSet Sum Problem
#         n = len(nums)

#         # Base Case
#         for i in range(n):
#             # print(i)
#             dp[i][0] = True

#         if nums[0] <= k:
#             dp[0][totalSum] = True

#         for i in range(1, n):
#             for target in range(1, k+1):
#                 notTake = dp[i-1][target]
#                 take = False
#                 if nums[i] <= target:
#                     take = dp[i-1][target-nums[i]]

#                 dp[i][target] = take or notTake

#         # Find the minimum difference
#         mini = 10**9
#         for s1 in range(totalSum//2+1):
#             if dp[n-1][s1] == True:
#                 s2 = abs(totalSum - s1)
#                 mini = min(mini, abs(s1 - s2))

#         return mini


obj = Solution()
nums = [3, 9, 7, 3]
nums = [-36, 36]
nums = [2, -1, 0, 4, -2, -9]
nums = [20, 19, 18, 20, 16]
print(obj.minDifference(nums, len(nums)))
# print(obj.minimumDifference(nums))


# [2,-1,0,4,-2,-9]

# sum = -6
