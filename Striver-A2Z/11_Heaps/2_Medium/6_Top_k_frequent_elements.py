# https://leetcode.com/problems/top-k-frequent-elements/

""" 
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.


Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1] 
"""
from collections import Counter
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        min_heap = []

        for ele in c:
            heapq.heappush(min_heap, (c[ele], ele))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        res = []
        while k > 0:
            res.append(heapq.heappop(min_heap)[1])
            k -= 1

        return res
