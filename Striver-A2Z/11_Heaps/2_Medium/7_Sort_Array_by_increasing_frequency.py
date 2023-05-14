# https://leetcode.com/problems/sort-array-by-increasing-frequency/description/
""" 
Given an array of integers nums, sort the array in increasing order based on the frequency 
of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

 

Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

Example 2:

Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.

Example 3:

Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1] 
"""

from collections import Counter
import heapq
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        c = Counter(nums)
        max_heap = []

        for i in c:
            # i is the element
            # c[i] is the freqency
            heapq.heappush(max_heap, (c[i], -1*i))

        res = []

        for _ in range(len(max_heap)):
            l = []
            freq, ele = heapq.heappop(max_heap)
            ele = -1*ele
            l = [ele]*(freq)
            res.extend(l)

        return res
