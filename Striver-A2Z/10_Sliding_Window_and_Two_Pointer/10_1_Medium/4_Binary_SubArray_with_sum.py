""" 
https://leetcode.com/problems/binary-subarrays-with-sum/description/

Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.
 

Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15
 """

from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        # countSubArrs(nums,goal) is a function that counts the subarrays which has sum less than or equal to goal.
        def countSubArr(goal):
            if goal < 0:
                return 0

            # Count all the subarray less than goal
            i = j = 0
            s = 0
            c = 0
            for j in range(len(nums)):
                s += nums[j]

                while s > goal:
                    s -= nums[i]
                    i += 1
                c += (j-i+1)
            return c

        return countSubArr(goal) - countSubArr(goal-1)
