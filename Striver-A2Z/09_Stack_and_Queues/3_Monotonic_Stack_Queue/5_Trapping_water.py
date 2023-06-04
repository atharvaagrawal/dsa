# https://leetcode.com/problems/trapping-rain-water/description/


""" 
Given n non-negative integers representing an elevation map where the 
width of each bar is 1, compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.



Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
"""


from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        if n == 1:
            return 0

        prefix = [-1]*n
        suffix = [-1]*n

        prefix[0] = height[0]
        suffix[-1] = height[-1]

        # Create Prefix and Suffix Array
        for i in range(1, n):
            if prefix[i-1] < height[i]:
                prefix[i] = height[i]
            else:
                prefix[i] = prefix[i-1]

        for i in range(n-2, -1, -1):
            if suffix[i+1] < height[i]:
                suffix[i] = height[i]
            else:
                suffix[i] = suffix[i+1]

        water = 0

        # Now Calculate
        for i in range(n):
            water += min(prefix[i], suffix[i])-height[i]

        return water
