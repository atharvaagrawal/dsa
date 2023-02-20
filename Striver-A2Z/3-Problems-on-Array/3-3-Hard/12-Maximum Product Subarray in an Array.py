""" 
Problem Statement: Given an array that contains both negative and positive integers, find the maximum product subarray.

Examples:

Example 1:
Input:
 Nums = [1,2,3,4,5,0]
Output:
 120
Explanation:
 In the given array, we can see 1×2×3×4×5 gives maximum product value.


Example 2:
Input:
 Nums = [1,2,-3,0,-4,-5]
Output:
 20
Explanation:
 In the given array, we can see (-4)×(-5) gives maximum product value.
"""

# Modified Kadane's Algorithm

def maxProduct(nums):
    prod1 = nums[0]
    prod2 = nums[0]
    res = nums[0]

    for i in range(1,len(nums)):
        temp = max(nums[i], prod1*nums[i], prod2*nums[i])

        prod2 = min(nums[i], prod1*nums[i], prod2*nums[i])

        prod1 = temp

        res = max(res,prod1)

    return res

nums = [2,3,-2,4]
nums = [-2,0,-1]
nums = [2]
print(maxProduct(nums))
