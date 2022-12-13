# https://leetcode.com/problems/maximum-subarray/
def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        max_end = 0
        
        for i in nums:
            max_end = max_end + i
            
            if max_so_far < max_end:
                max_so_far = max_end
            if max_end < 0:
                max_end = 0
        
        return max_so_far   