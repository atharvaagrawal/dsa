# https://leetcode.com/problems/longest-consecutive-sequence/description/ 


""" Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
Therefore its length is 4.
 """
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 0,3,7,2,5,8,4,6,0,1
        # if len(nums) == 0:
        #     return 0
        #     # 1,2,0,1
        #     # 0 1 1 2
        #     # 
        # s = set(nums)
        # nums = list(s)
        # nums.sort()
        # m = 0
        # ct = 0
        # for i in range(len(nums)-1):
        #     if nums[i]+1 == nums[i+1]:
        #         ct +=1
        #     else:
        #         m = max(ct+1,m)
        #         ct = 0
                
        # m = max(ct+1,m)
 
        # return m

        # Without Using Sort
        d = dict()
        for i in nums:
            d[i] = 0
        
        l = 0
        ct = 0
        
        print(d)

        for i in range(len(nums)):
            if nums[i]-1 in d:               
                ct +=1
                while True:
                    if nums[i]+1 in d:
                        ct += 1
                    else:
                        break
                    i+=1
            else:
                print(ct+1)
                l = max(ct+1,l)
                ct = 0

        l = max(ct+1,l)

        return l