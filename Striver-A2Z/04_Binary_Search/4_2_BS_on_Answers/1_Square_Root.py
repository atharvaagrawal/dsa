# https://practice.geeksforgeeks.org/problems/square-root/0

""" 
Given an integer x, find the square root of x. If x is not a perfect square, 
then return floor(√x).
 

Example 1:

Input:
x = 5
Output: 2
Explanation: Since, 5 is not a perfect 
square, floor of square_root of 5 is 2.

Example 2:

Input:
x = 4
Output: 2
Explanation: Since, 4 is a perfect 
square, so its square root is 2.
"""


class Solution:
    def floorSqrt(self, x):

        low = 1
        high = x
        mid = 0
        ans = None
        while low <= high:

            mid = (low+high)//2

            nsquare = mid**2

            if nsquare == x:
                return mid
            elif nsquare > x:
                high = mid - 1
            else:
                ans = mid  # As we want the lower bound if ans not present
                low = mid + 1

        return ans
