# https://leetcode.com/problems/search-a-2d-matrix/description/

""" 
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false 
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        prev = float('inf')

        for i in range(len(matrix)):

            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True

                if matrix[i][j] > target:
                    break

            prev = matrix[i][len(matrix[0])-1]

            if target < prev:
                return False

        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binarySearch(row):

            low = 0
            high = len(matrix[0])-1

            while low <= high:

                mid = (low+high)//2

                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    high = mid-1
                else:
                    low = mid+1

            return False

        for row in range(len(matrix)):

            if target <= matrix[row][-1]:
                return binarySearch(row)

        return False
