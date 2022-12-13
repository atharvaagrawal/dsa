# https://leetcode.com/problems/sort-colors/
# Dutch National Flag problem
def sortColors(self, nums: List[int]) -> None:
        lo = 0
        mid = 0
        high = len(nums)-1
        
        while( mid <= high):
            if nums[mid] == 0:
                nums[lo],nums[mid] = nums[mid],nums[lo]
                lo+=1
                mid+=1
            elif nums[mid] == 1:
                mid+=1
            else:
                nums[high],nums[mid] = nums[mid],nums[high]
                high-=1
                
        print(nums)