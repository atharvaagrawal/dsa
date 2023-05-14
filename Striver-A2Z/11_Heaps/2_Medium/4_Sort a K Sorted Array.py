# https://practice.geeksforgeeks.org/problems/nearly-sorted-1587115620/1

""" 
Given an array of n elements, where each element is at most k away from its target position, 
you need to sort the array optimally.

Example 1:
Input:
n = 7, k = 3
arr[] = {6,5,3,2,8,10,9}

Output: 2 3 5 6 8 9 10
Explanation: The sorted array will be
2 3 5 6 8 9 10

Example 2:
Input:
n = 5, k = 2
arr[] = {3,1,4,2,5}

Output: 1 2 3 4 5 
"""
from queue import PriorityQueue


class Solution:
    def nearlySorted(self, a, n, k):
        q = PriorityQueue()
        res = []

        # it will of size k
        for i in a:
            q.put(i)
            if q.qsize() > k:
                res.append(q.get())

        while not q.empty():
            res.append(q.get())

        return res
