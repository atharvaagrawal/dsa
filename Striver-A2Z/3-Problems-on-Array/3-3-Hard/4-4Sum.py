class Solution:
    def fourSum(self, nums, target):
        # a+b+c+d = target
        # Two Pointer Approach

        nums.sort()
        n = len(nums)
        
        res = []
        
        i = 0

        while i < n-2:
            j = i+1
            while j < n-1:
                lo = j+1
                high = n-1

                remain = target - (nums[i]+nums[j])
                
                while lo < high:
                    if nums[lo]+nums[high] == remain:
                        res.append([nums[i],nums[j],nums[lo],nums[high]])

                        while lo<high and nums[lo] == nums[lo+1]:
                            lo+=1
                        while lo<high and nums[high] == nums[high-1]:
                            high-=1
                        lo+=1
                        high-=1

                    elif nums[lo]+nums[high] < remain:
                        lo+=1
                    else:
                        high-=1
              
                while j < n-1 and nums[j] == nums[j+1]:
                    j+=1
                j+=1
            
            while i < n-1 and nums[i] == nums[i+1]:
                i+=1
            i+=1

        return res
