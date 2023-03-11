""" 
Partition Equal Subset Sum

Given an integer array nums, return true if you can partition the array into two subsets such that 
the sum of the elements in both subsets is equal or false otherwise.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(i for i in nums)
        
        if total%2 != 0:
            return False

        dp = [[-1 for i in range(total//2+1)] for i in range(len(nums))]
        
        # Memorization
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
            
        #return solve(len(nums)-1,total//2)

        if len(nums) <= 1:
            return False

        # Tabulation
        def solve2():
            k = total//2

            dp = [[False for i in range(k+1)] for i in range(len(nums))]
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
                    if nums[i] < target:
                        take = dp[i-1][target-nums[i]]
                    
                    dp[i][target] = take or notTake
            
            return dp[n-1][k]
        
        return solve2()

