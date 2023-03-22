# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binarySearch(low,high,arr):
            mid = (low+high)//2

            while low <= high:
                # print(arr[mid],target)
                if arr[mid] == target:
                    return mid
                
                if arr[mid] > target:
                    high = mid-1
                elif arr[mid] < target:
                    low = mid+1
                
                mid = (low+high)//2 
            
            return -1
        
        def findRotated(nums):
            count = 0
           
            for i in range(1,len(nums)):
                if nums[i] < nums[i-1]:
                    return i
        
            return -1
        
        rotate_position = findRotated(nums)
        print(rotate_position)
        if rotate_position == -1:
            return binarySearch(0,len(nums)-1,nums)
        return max(binarySearch(0,rotate_position-1,nums),binarySearch(rotate_position,len(nums)-1,nums))
                    