# https://practice.geeksforgeeks.org/problems/max-rectangle/1

""" 
Given a binary matrix M of size n X m. Find the maximum area of a rectangle formed only of 1s in the given matrix.

Example 1:

Input:
n = 4, m = 4
M[][] = {{0 1 1 0},
         {1 1 1 1},
         {1 1 1 1},
         {1 1 0 0}}
Output: 8
Explanation: For the above test case the
matrix will look like
0 1 1 0
1 1 1 1
1 1 1 1
1 1 0 0
the max size rectangle is 
1 1 1 1
1 1 1 1
and area is 4 *2 = 8.
"""


class Solution:

    def maxArea(self, M, n, m):

        def solve(heights):
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

            # print(right_smaller)
            # print(left_smaller)

            # Now we have the left and right smaller
            for i in range(n):
                maxArea = max(
                    maxArea, (right_smaller[i]-left_smaller[i]+1) * heights[i])

            return maxArea

        row = [0]*m

        maxArea = 0

        for level in range(n):

            # For each row
            for i in range(m):
                row[i] += M[level][i]
                if M[level][i] == 0:
                    row[i] = 0

            maxArea = max(maxArea, solve(row))

        return maxArea
