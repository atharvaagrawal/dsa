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

# Recursion


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


N = 6
arr = [3, 34, 4, 12, 5, 2]
sum = 9

N = 6
arr = [3, 34, 4, 12, 5, 2]
sum = 30


obj = Solution()
obj.isSubsetSum(N, arr, sum)
