# https://practice.geeksforgeeks.org/problems/find-nth-root-of-m5843/1
""" 
You are given 2 numbers (n , m); the task is to find n√m (nth root of m).
 
Example 1:

Input: n = 2, m = 9
Output: 3
Explanation: 32 = 9

Example 2:
Input: n = 3, m = 9
Output: -1
Explanation: 3rd root of 9 is not integer.
"""


class Solution:
    def NthRoot(self, n, m):

        low = 1
        high = (m//n + 1)

        while low <= high:

            mid = (low+high)//2

            res = mid**n

            if res == m:
                return mid

            if res > m:
                high = mid-1
            else:
                low = mid+1

        return -1
