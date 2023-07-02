# https://practice.geeksforgeeks.org/problems/swap-two-numbers3844/1

""" 
Swap given two numbers and print them. (Try to do it without a temporary variable.) and return it.

Example 1:

Input: a = 13, b = 9
Output: 9 13
Explanation: after swapping it
becomes 9 and 13.
"""


class Solution:
    def get(self, a, b):
        # code here
        a = a ^ b
        b = a ^ b
        a = a ^ b

        return [a, b]
