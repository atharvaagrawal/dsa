""" 
Given an array arr[] of non-negative integers and an integer sum, the task is to count all 
subsets of the given array with a sum equal to a given sum.

Note: Answer can be very large, so, output answer modulo 10e9+7

Example 1:
Input: N = 6, arr[] = {2, 3, 5, 6, 8, 10}
       sum = 10
Output: 3
Explanation: {2, 3, 5}, {2, 8}, {10}

Example 2:
Input: N = 5, arr[] = {1, 2, 3, 4, 5}
       sum = 10
Output: 3
Explanation: {1, 2, 3, 4}, {1, 4, 5}, 
             {2, 3, 5}
"""

# Recursion


class Solution:
    def perfectSum(self, arr, n, sum):
        
        count = 0       
        
        k = sum 
        dp = [[False for i in range(k+1)] for i in range(n) ]

        for i in range(n):
            dp[i][0] = True
        
        if arr[0] <= k:
            dp[0][arr[0]] = True

        for i in range(1,n):
            for target in range(1,k+1):
                notTake = dp[i-1][target]
                take = False

                if arr[i] <= target:
                    take = dp[i-1][target - arr[i]]
                
                dp[i][target] = take or notTake
                if dp[i][target] and i!=0 and i != n-1:
                    count+=1
        # Now the dp[n-1][0..k] will contain all the possible yes
 
        for i in range(1,k+1):
            if dp[n-1][i] == True:
                count+=0

        print(count)
        return count                
obj = Solution()

arr = [2, 3, 5, 6, 8, 10]
sum = 10
n = len(arr)
obj.perfectSum(arr,n,sum)



