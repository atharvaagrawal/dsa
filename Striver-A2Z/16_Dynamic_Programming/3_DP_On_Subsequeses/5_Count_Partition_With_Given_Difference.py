""" 
https://practice.geeksforgeeks.org/problems/partitions-with-given-difference/1

Given an array arr, partition it into two subsets(possibly empty) such that their union is the original array. 
Let the sum of the element of these two subsets be S1 and S2. 

Given a difference d, count the number of partitions in which S1 is greater than or equal to S2 and 
the difference S1 and S2 is equal to d. since the answer may be large return it modulo 109 + 7.


Example 1:
Input:
n = 4, d = 3
arr[] =  { 5, 2, 6, 4}
Output:
1
Explanation:
There is only one possible partition of this array. Partition : {6, 4}, {5, 2}. The subset difference between subset sum is: (6 + 4) - (5 + 2) = 3.

Example 2:
Input:
n = 4, d = 0
arr[] = {1, 1, 1, 1}
Output:
6 
"""


# Memoization
class Solution:
    def countPartitions(self, n, d, arr):
        # Code here
        totalSum = sum(arr)

        s1 = totalSum - d

        if s1 < 0:
            return 0

        if (totalSum-d) % 2 == 1:
            return 0

        s2 = (totalSum-d) // 2

        dp = [[-1 for i in range(s2+1)] for j in range(n+1)]

        # Subset partition difference
        def solve(ind, target):

            if ind == 0:
                if target == 0 and arr[0] == 0:
                    return 2
                if target == 0 or target == arr[0]:
                    return 1
                return 0

            if dp[ind][target] != -1:
                return dp[ind][target]

            take = 0
            notTake = 0

            # Take or Not Take
            if arr[ind] <= target:
                take = solve(ind-1, target-arr[ind])
            notTake = solve(ind-1, target)

            dp[ind][target] = (take + notTake) % (10**9+7)

            return dp[ind][target]

        return solve(n-1, s2) % (10**9+7)


# Tabulation
class Solution:
    def countPartitions(self, n, d, arr):
        totalSum = sum(arr)

        s1 = totalSum - d
        if s1 < 0:
            return 0

        if (totalSum-d) % 2 == 1:
            return 0

        s2 = (totalSum-d)//2

        dp = [[0 for i in range(s2+1)] for j in range(n)]

        # Base Case
        if arr[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1

        if arr[0] != 0 and arr[0] <= s2:
            dp[0][arr[0]] = 1

        for ind in range(1, n):
            for target in range(s2+1):
                notTake = dp[ind-1][target]
                take = 0
                if arr[ind] <= target:
                    take = dp[ind-1][target-arr[ind]]

                dp[ind][target] = (notTake+take) % (10**9+7)

        return dp[n-1][s2]
