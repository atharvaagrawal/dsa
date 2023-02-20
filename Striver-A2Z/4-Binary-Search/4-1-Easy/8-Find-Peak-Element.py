from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        left = 0
        right = n-1

        while left < right:
            mid = (left+right)//2
            
            if (mid == 0):
                if nums[0] > nums[1]:
                    return 0
                else:
                    return 1
                    
            if (mid == n-1 ):
                if nums[n - 1] > nums[n - 2]:
                    return  n-1
                else:
                    return n-2

            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid  

            if nums[mid] < nums[mid-1]:
                right = mid-1
            else:
                left = mid+1

        return left


nums = [6,5,4,3,2,3,2]
obj = Solution()
print(obj.findPeakElement(nums))