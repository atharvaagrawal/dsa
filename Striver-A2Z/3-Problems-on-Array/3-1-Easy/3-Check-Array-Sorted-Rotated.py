# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/


class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        
        for i in range(len(nums)):
            if nums[i] < nums[i-1]:
                count += 1
                
        return count <= 1