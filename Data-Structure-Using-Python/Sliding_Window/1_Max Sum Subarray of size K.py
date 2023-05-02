""" 
https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1

Given an array of integers Arr of size N and a number K. Return the maximum sum of a subarray of size K.

Example 1:
Input:
N = 4, K = 2
Arr = [100, 200, 300, 400]
Output:
700

Explanation:
Arr3  + Arr4 =700,
which is maximum.
 

Example 2:
Input:
N = 4, K = 4
Arr = [100, 200, 300, 400]
Output:
1000

Explanation:
Arr1 + Arr2 + Arr3  
+ Arr4 =1000,
which is maximum. 
"""


class Solution:
    def maximumSumSubarray(self, k, nums, N):

        # We can take a window of size k
        # And can calculate the res

        ans = 0
        i = j = 0
        curr = 0

        # 1,5,4,2,9,9,9
        # 1,5,4
        #   5,4,2
        c = 0
        for j in range(len(nums)):
            curr += nums[j]
            c += 1
            if c > k:
                curr -= nums[i]
                i += 1
                c -= 1
            # print(nums[j],i,j,curr,c)
            ans = max(ans, curr)

        return ans
