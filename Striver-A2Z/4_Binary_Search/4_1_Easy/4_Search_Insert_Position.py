""" 
Given a sorted array of distinct integers and a target value, return the index if 
the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4 
"""

from typing import List 

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        flag = 0
         
        if target > nums[high]:
            return high+1
        if target < nums[0]:
            return 0

        while low <= high:
            mid = (low+high)//2
            # 1
            if nums[mid] == target:
                return mid
        
            if target < nums[mid]:
                high = mid - 1  
            elif target > nums[mid]:
                low = mid + 1
        
        return low