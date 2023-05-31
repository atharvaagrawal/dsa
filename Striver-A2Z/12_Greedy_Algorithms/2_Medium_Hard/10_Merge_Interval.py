# https://leetcode.com/problems/merge-intervals/

""" 
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the 
non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

from typing import List


class Solution:
    def merge(self, l: List[List[int]]) -> List[List[int]]:
        # Sort the 2d array by start
        l.sort()
        res = []
        s, e = l[0][0], l[0][1]

        for i in range(len(l)):
            start, end = l[i][0], l[i][1]

            if start <= e:
                e = max(end, e)
            else:
                res.append([s, e])
                s, e = start, end

        res.append([s, e])

        return res
