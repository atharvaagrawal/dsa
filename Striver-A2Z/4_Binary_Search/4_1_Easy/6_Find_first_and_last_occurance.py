""" 
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solutions/3190044/easy-python-binary-search-solution/

Given an array of integers nums sorted in non-decreasing order, find the starting and 
ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1] 

"""
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s = -1
        e = -1

        if len(nums) == 0:
            return [s,e]
        
        def binarySearch(nums,left,right):        
            mid = (left+right)//2

            while left <= right and right < len(nums):
                if nums[mid] == target:
                    s = binarySearchLeft(nums,0,mid-1,mid)
                    e = binarySearchRight(nums,mid+1,len(nums)-1,mid)
                    return [s,e]
                    
                if nums[mid] > target:
                    right = mid - 1

                if nums[mid] < target:
                    left = mid+1

                if left > right:
                    return [-1,-1]

                mid = (left+right)//2
            return [s,e]

        def binarySearchLeft(nums,left,right,res):        
            mid = (left+right)//2

            while left <= right and right < len(nums):
                if nums[mid] == target:
                    return binarySearchLeft(nums,0,mid-1,mid)

                if nums[mid] > target:
                    right = mid - 1

                if nums[mid] < target:
                    left = mid+1

                if left > right:
                    return res

                mid = (left+right)//2
            return res

        def binarySearchRight(nums,left,right,res):        
            mid = (left+right)//2

            while left <= right and right < len(nums):
                if nums[mid] == target:
                    return binarySearchRight(nums,mid+1,len(nums)-1,mid)
                    
                if nums[mid] > target:
                    right = mid - 1

                if nums[mid] < target:
                    left = mid+1

                if left > right:
                    return res

                mid = (left+right)//2
            return res

        return binarySearch(nums,0,len(nums)-1)

obj = Solution()
nums = [5,7,7,8,8,10]
target = 8
nums = [5,7,7,8,8,10] 
target = 6
print( obj.searchRange(nums,target))