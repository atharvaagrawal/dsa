# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description
class Solution:
    def findMin(self, nums: List[int]) -> int:

        def binarySearch(nums):
            left = 0
            right = len(nums)-1
            
            if len(nums) == 1:
                return nums[0]

            if nums[left] < nums[right]:
                return nums[left]

            while left < right:
                mid = (left+right)//2
                
                lefNum = nums[left]
                midNum = nums[mid]
                leftofMid = nums[mid-1]
                rightofMid = nums[mid+1]

                if nums[mid] > rightofMid:
                    return rightofMid
                elif midNum < leftofMid:
                    return midNum
                
                if midNum > lefNum:
                    left = mid + 1
                else:
                    right = mid -1
        
        
        return binarySearch(nums)