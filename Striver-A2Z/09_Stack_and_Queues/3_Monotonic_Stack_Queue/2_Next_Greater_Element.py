# https://leetcode.com/problems/next-greater-element-ii/description/

""" 
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), 
return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in
the array, which means you could search circularly to find its next greater number. 
If it doesn't exist, return -1 for this number.

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.

Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]

"""

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1]*len(nums)

        stack = []

        for i in range(2*len(nums)-1, -1, -1):
            while len(stack) > 0 and stack[-1] <= nums[i % len(nums)]:
                stack.pop()

            if i < len(nums):
                if len(stack) > 0:
                    res[i] = stack[-1]
                else:
                    res[i] = -1

            stack.append(nums[i % len(nums)])

        return res
