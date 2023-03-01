""" 
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1 
"""

from collections import defaultdict

def singleNumber(nums):
        # d = {}
        # d = defaultdict(lambda: 0,d)

        # for i in nums:
        #     d[i] +=1
        
        # for i in d.keys():
        #     if d[i] == 1:
        #         return i
        
        ones = 0
        for i in nums:
            ones = ones ^ i
        
        return ones