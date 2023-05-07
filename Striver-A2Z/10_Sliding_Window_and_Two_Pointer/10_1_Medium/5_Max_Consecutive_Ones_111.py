""" 
https://leetcode.com/problems/max-consecutive-ones-iii/

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at 
most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        zero_count = 0
        ans = 0

        # Our Window
        i = j = 0

        while j < len(nums):
            if nums[j] == 1:
                pass
            elif nums[j] == 0:
                zero_count += 1

                # Check if zero count is greater than k
                while zero_count > k:
                    # Move i until zero_count is equal or less than k
                    if nums[i] == 0:
                        zero_count -= 1
                    i += 1

            ans = max(ans, j-i+1)
            j += 1
        return ans
