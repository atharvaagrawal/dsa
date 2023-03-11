'''
Given an array of non-negative integers, and a value sum, determine if there is a subset of the given set with 
sum equal to given sum. 

Example 1:
Input:
N = 6
arr[] = {3, 34, 4, 12, 5, 2}
sum = 9

Output: 1 

Explanation: Here there exists a subset with
sum = 9, 4+3+2 = 9.

Example 2:
Input:
N = 6
arr[] = {3, 34, 4, 12, 5, 2}
sum = 30

Output: 0 

Explanation: There is no subset with sum 30.
'''

from typing import List

# Recursion
""" 
class Solution:
    def isSubsetSum(self, N, arr, sum):
        def solve(res, n):
            if res == sum:
                return 1
            if n == 0:
                res += arr[n]
                if res == sum:
                    return 1
                else:
                    return 0

            # pick and not-pick
            return max(solve(res+arr[n], n-1), solve(res, n-1))

        print(solve(0, N-1)) 
"""

# Memorization
""" class Solution:
    def isSubsetSum(self, N, nums, sum):
        dp = [[-1 for i in range(sum+1)] for i in range(len(nums))]
        
        def solve(n,target):    
            if target == 0:
                return 1
            if n == 0:
                return target == nums[0]
            
            if dp[n][target] != -1:
                return dp[n][target]

            notTake = solve(n-1,target)

            take = False
            if nums[n] <= target:
                take = solve(n-1,target-nums[n])
            
            dp[n][target] = take or notTake

            return dp[n][target]
        
        return solve(N-1,sum) 
"""


# Tabulation
class Solution:
    def isSubsetSum(self, N, nums, sum):
        
        def solve():
            k = sum

            dp = [[False for i in range(sum+1)] for i in range(len(nums))]
            n = len(nums)
            
            # Base Case
            for i in range(n):
                dp[i][0] = True

            if nums[0] <= k:
                dp[0][nums[0]] = True
            
            for i in range(1,n):
                for target in range(1,k+1):
                    notTake = dp[i-1][target]

                    take = False
                    if nums[i] <= target:
                        take = dp[i-1][target-nums[i]]
                    
                    dp[i][target] = take or notTake
            
            print(dp)
            return dp[n-1][k]
        
        return solve()

N = 6
arr = [3, 34, 4, 12, 5, 2]
sum = 9

N = 6
arr = [3, 34, 4, 12, 5, 2]
sum = 30

arr = [2, 3, 5, 6, 8, 10]
sum = 10
N = len(arr)

obj = Solution()
obj.isSubsetSum(N, arr, sum)
