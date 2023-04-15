# https://leetcode.com/problems/subsets/
""" 
Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
"""
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def solve(ind,op):
            if ind == n:
                res.append(op.copy())
                return

            op.append(nums[ind])
            solve(ind+1,op)
            op.pop()
            solve(ind+1,op)

        solve(0,[])
        # print(res)
        return res
        
obj = Solution()

nums = [1,2,3]

print(obj.subsets(nums))