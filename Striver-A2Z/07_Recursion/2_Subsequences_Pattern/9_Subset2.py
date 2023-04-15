# https://leetcode.com/problems/subsets-ii/description/

""" Given an integer array nums that may contain duplicates, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]] """

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []
        n = len(nums)
        def solve(ind,l):
            res.append(l.copy())
            
            for i in range(ind,n):
                if i > ind and nums[i] == nums[i-1]:
                    continue
                l.append(nums[i])
                solve(i+1,l)
                l.pop()
            
        solve(0,[])
        return res