""" 
Example 1:
Input:
arr = {7,1,6,0}, k = 7

Output: Length of the longest subarray with sum K is 3
Explanation:
 1 + 6 + 0 = 7, it is the longest subarray with sum 7 and length 3.

Example 2:
Input: 
arr = {2,3,5,1,9}, k = 10
Output: Length of the longest subarray with sum K is 3
Explanation: 2 + 3 + 5 = 10, it is the longest subarray with sum 10 and length 3 
"""

def subarraySum(nums,k):
    res = 0
    d = dict()
    d[0] = 1
    preSum = 0

    for i in nums:
        preSum += i

        if preSum - k in d.keys():
            res += d[preSum-k]
        
        d[preSum] = d.get(preSum,0) + 1
    
    return res


# def subarraySum(self, nums: List[int], k: int) -> int:
        # TLE
        # m = 0

        # for i in range(len(nums)):
        #     ct = 0
        #     for j in range(i,len(nums)):
        #         ct += nums[j]
        #         if(ct == k):
        #             m +=1
        # return m