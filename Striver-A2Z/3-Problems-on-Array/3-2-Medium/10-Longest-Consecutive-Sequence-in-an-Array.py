# https://leetcode.com/problems/longest-consecutive-sequence/description/ 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 0,3,7,2,5,8,4,6,0,1
        if len(nums) == 0:
            return 0
            # 1,2,0,1
            # 0 1 1 2
            # 
        s = set(nums)
        nums = list(s)
        nums.sort()
        m = 0
        ct = 0
        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                ct +=1
            else:
                m = max(ct+1,m)
                ct = 0
                
        m = max(ct+1,m)
 
        return m