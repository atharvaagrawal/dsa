class Solution:
    def threeSum(self, nums):
        
        # Two Pointer Approach 
        # a+b+c = 0
        # b+c = -a
        
        ptr1 = 0
        nums.sort()
        res = []

        while ptr1 < len(nums):
            lo = ptr1+1
            high = len(nums)-1
            
            while lo < len(nums) and lo < high:
                if nums[lo]+nums[high] == -(nums[ptr1]):
                    res.append([nums[ptr1],nums[lo],nums[high]])

                    while lo<high and nums[lo] == nums[lo+1]:
                        lo+=1
                    while lo<high and nums[high] == nums[high-1]:
                        high-=1

                    lo+=1
                    high-=1
                    
                elif nums[lo]+nums[high] < -(nums[ptr1]):
                    lo +=1
                else:
                    high -=1

            while ptr1 < len(nums)-1 and nums[ptr1] == nums[ptr1+1]:
                ptr1+=1
            
            ptr1+=1

        return res
                