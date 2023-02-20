# Given an array arr[] of size N, check if it is sorted in non-decreasing order or not. 
""" 
Example 1:
Input:
N = 5
arr[] = {10, 20, 30, 40, 50}
Output: 1
Explanation: The given array is sorted.

Example 2:
Input:
N = 6
arr[] = {90, 80, 100, 70, 40, 30}
Output: 0
Explanation: The given array is not sorted. 
"""

class Solution:
    def arraySortedOrNot(self, arr, n):
        prev = arr[0]
        flag = 0
        for i in range(1,len(arr)):
            if arr[i] >= prev:
                pass
            else:
                flag = 1
                break
            prev = arr[i]
    
        if flag:
            return 0 
        else:
            return 1