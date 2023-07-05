# https://leetcode.com/problems/split-array-largest-sum/description//


"""
Given an integer array nums and an integer k, split nums into k non-empty subarrays such 
that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.


Example 1:

Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.

Example 2:

Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
"""


from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def check(min_num):
            n = 1
            s = 0

            for i in range(len(nums)):
                if s+nums[i] <= min_num:
                    s += nums[i]
                else:
                    n += 1
                    s = nums[i]

            return n

        # The range will be max(nums) if k == len(nums)
        # till the sum(nums) if k == 1

        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = (low+high)//2

           # It will check the minium users will required
            if check(mid) > k:
                low = mid+1
            else:
                high = mid-1

        return low
