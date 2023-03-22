""" 
Given a sorted array Arr of size N and a number X, you need to find the number of 
occurrences of X in Arr.

Example 1:
Input:
N = 7, X = 2
Arr[] = {1, 1, 2, 2, 2, 2, 3}
Output: 4

Explanation: 2 occurs 4 times in the given array.
 """
def count(self,nums, n, target):
        if len(nums) == 0:
            return 0
            
        def binarySearch(nums,left,right):        
            mid = (left+right)//2
            count = 0 
            
            while left <= right and right < len(nums):
                if nums[mid] == target:
                    left = mid-1
                    right = mid+1
                    count = 1
                    
                    while left >= 0 and nums[left] == target:
                        count+=1
                        left-=1
                        
                    while right < len(nums) and nums[right] == target:
                        count+=1
                        right+=1
                    
                    return count
                    
                if nums[mid] > target:
                    right = mid - 1

                if nums[mid] < target:
                    left = mid+1

                if left > right:
                    return 0

                mid = (left+right)//2
            return 0 


        return binarySearch(nums,0,len(nums)-1)