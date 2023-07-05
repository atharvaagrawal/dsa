# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
""" 
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
w"""


from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        # Formula: (right_smaller[i] - left_smaller[i] + 1) * heights[i]
        n = len(heights)

        right_smaller = [-1]*n
        left_smaller = []

        stack = []  # Index will be store

        # Calculate Left Smaller
        for i in range(n):

            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()

            if not stack:
                left_smaller.append(0)
            else:
                left_smaller.append(stack[-1]+1)

            stack.append(i)

        stack = []

        # Calculate Right Smaller
        for i in range(n-1, -1, -1):

            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()

            if not stack:
                right_smaller[i] = n-1
            else:
                right_smaller[i] = stack[-1]-1

            stack.append(i)

        print(right_smaller)
        print(left_smaller)

        # Now we have the left and right smaller
        for i in range(n):
            maxArea = max(
                maxArea, (right_smaller[i]-left_smaller[i]+1) * heights[i])

        return maxArea


obj = Solution()
heights = [10, 20, 30, 50, 10, 70, 30]
obj.largestRectangleArea(heights)
