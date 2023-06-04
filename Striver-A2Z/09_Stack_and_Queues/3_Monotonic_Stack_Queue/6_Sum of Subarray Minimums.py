# https://leetcode.com/problems/sum-of-subarray-minimums/

""" 
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) 
subarray of arr. Since the answer may be large, return the answer modulo 10^9 + 7. 

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

Example 2:

Input: arr = [11,81,94,43,3]
Output: 444
"""

from typing import List


# BruteForce: TLE
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        def printSubArrays(arr, start, end, res):
            if end == len(arr):
                return res
            elif start > end:
                return printSubArrays(arr, 0, end + 1, res)
            else:
                curr = min(arr[start:end + 1])
                return printSubArrays(arr, start + 1, end, curr+res)

        x = printSubArrays(arr, 0, 0, 0)

        return x


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # Stack
        s1 = []
        s2 = []

        n = len(arr)

        next_smaller = [-1]*n
        prev_smaller = [-1]*n

        for i in range(n):
            next_smaller[i] = n-i-1
            prev_smaller[i] = i

        for i in range(n):

            while s1 and arr[s1[-1]] > arr[i]:
                next_smaller[s1[-1]] = i-s1[-1]-1
                s1.pop()

            s1.append(i)

        for i in range(n-1, -1, -1):

            while s2 and arr[s2[-1]] >= arr[i]:
                prev_smaller[s2[-1]] = s2[-1]-i-1
                s2.pop()

            s2.append(i)

        ans = 0
        mod = 10**9+7

        for i in range(n):
            ans += (arr[i]*(prev_smaller[i]+1))*(next_smaller[i]+1)

            ans = ans % mod

        return ans
