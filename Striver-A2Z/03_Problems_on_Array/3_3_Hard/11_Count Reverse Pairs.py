""" 
Problem Statement: Given an array of numbers, you need to return the count of reverse pairs. 
Reverse Pairs are those pairs where i<j and arr[i]>2*arr[j].

Example 1:
Input: N = 5, array[] = {1,3,2,3,1)
Output: 2 
Explanation: The pairs are (3, 1) and (3, 1) as from both the pairs the condition arr[i] > 2*arr[j] is satisfied.

Example 2:
Input: N = 4, array[] = {3,2,1,4}
Output: 1
Explaination: There is only 1 pair  ( 3 , 1 ) that satisfy the condition arr[i] > 2*arr[j] 
"""

from typing import List
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(arr,left,right):    
            rev_pairs = 0

            if left < right:
                mid = (left+right)//2

                rev_pairs += mergeSort(arr,left,mid)
                rev_pairs += mergeSort(arr, mid+1, right)
                rev_pairs += merge(arr,left,mid,right)
            
            return rev_pairs

        def merge(arr,left,mid,right):
            i = left
            j = mid+1
            k = left
            temp_arr = []

            rev_pairs = 0
            
            while i <= mid and j <=right:
                if arr[i] > 2*arr[j]:
                    rev_pairs+= (mid-i+1)
                    j+=1
                else:
                    i+=1

            i = left
            j = mid+1

            while i <= mid and j <= right:
                if arr[i] < arr[j]:
                    temp_arr.append(arr[i])
                    i+=1
                else:
                    temp_arr.append(arr[j])
                    j+=1
                

            while i <= mid:
                temp_arr.append(arr[i])
                i+=1
                

            while j <= right:
                temp_arr.append(arr[j])
                j+=1

            for i in range(left,right+1):
                arr[i] = temp_arr[i-left]

            return rev_pairs


        n = len(nums)
        
        return mergeSort(nums,0,n-1)

arr = [1,3,2,3,1]
# arr = [3,2,1,4]
obj = Solution()
res = obj.reversePairs(arr)
print("Reverse Pairs Count:",res)
print(arr)

# 0 4
# 2 

# 1,3,2,3,1
# [1, 3, 2, 3, 1]
# [1, 2, 3, 3, 1]
# [1, 2, 3, 1, 3]
# [1, 1, 2, 3, 3]
# [1, 1, 2, 3, 3]

# [1, 3, 0, 0, 0]
# [1, 2, 3, 0, 0]
# [0, 0, 0, 1, 3]

# 1 2 3  1 3
# 1      1 3

# temp_arr: 1 

# [1, 1, 2, 3, 3]
# [1, 1, 2, 3, 3]
