# https://practice.geeksforgeeks.org/problems/perfect-sum-problem5633/1

# Given an array arr[] of non-negative integers and an integer sum, the task is to count 
# all subsets of the given array with a sum equal to a given sum.
# Note: Answer can be very large, so, output answer modulo 109+7

""" 
Input: N = 6, arr[] = {2, 3, 5, 6, 8, 10}
       sum = 10
Output: 3
Explanation: {2, 3, 5}, {2, 8}, {10}

Input: N = 5, arr[] = {1, 2, 3, 4, 5}
       sum = 10
Output: 3
Explanation: {1, 2, 3, 4}, {1, 4, 5}, {2, 3, 5}
"""

class Solution:
    def perfectSum(self, arr, n, sum):
        cnt = [0]

        def solve(ind,k):            
            if ind == n:
                if sum == k:
                    return 1
                return 0

            return solve(ind+1,k+arr[ind])  + solve(ind+1,k) 
        
        print(solve(0,0))
        # print(cnt[0])

        return cnt[0] % 10**9+7

            # Take

obj = Solution()

arr = [2, 3, 5, 6, 8, 10]
n = 6
sum = 10

n = 2
sum = 1
arr = [1,0]

obj.perfectSum(arr,n,sum)