# https://takeuforward.org/data-structure/subarray-with-given-sum/


""" 
Given an array and a sum k, generate the subarray whose elements sum to k.

Example 1:
Input:
 arr = {1, 7, 3, 9}, k = 10

Output: 7 3
Explanation:
 Of all the subarrays, 7 and 3 sums to 10.

Example 2:
Input: arr = {2,1,3,4,5,6}, k = 10
Output: 2 1 3 4
Explanation: Of all the subarrays, 2, 1, 3 and 4 sums to 1
 """
def maxSubArray(nums):
        max_so_far = nums[0]
        max_end = 0
        arr = []
        res = []
        for i in nums:
            max_end = max_end + i
            arr.append(i)

            if max_so_far < max_end:
                max_so_far = max_end
                res = arr

            if max_end < 0:
                max_end = 0
                arr = []

        print(max_so_far)
        print(res)

nums = [1, 7, 3, 9]
nums = [-2,1,3,4,-5,6]
maxSubArray(nums)
