# https://leetcode.com/problems/kth-missing-positive-number/description/


""" 
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
"""

from typing import List


# BruteForce
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        missing_array = []

        for i in range(1, max(arr)+k+1):
            if i not in arr:
                missing_array.append(i)

        low = 1
        return missing_array[k-1]


# Optimal
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        low = 0
        high = len(arr)-1

        while low <= high:

            mid = (low+high)//2

            missing_num = arr[mid]-(mid+1)

            if missing_num < k:
                low = mid + 1
            else:
                high = mid - 1

        # Once they crosses we will get two nearby index

        return high + k + 1
