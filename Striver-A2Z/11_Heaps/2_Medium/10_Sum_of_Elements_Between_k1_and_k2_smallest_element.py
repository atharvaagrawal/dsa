# https://practice.geeksforgeeks.org/problems/sum-of-elements-between-k1th-and-k2th-smallest-elements3133/1

""" 
Given an array A[] of N positive integers and two positive integers K1 and K2. 
Find the sum of all elements between K1th and K2th smallest elements of the array. 
It may be assumed that (1 <= k1 < k2 <= n).


Example 1:

Input:
N  = 7
A[] = {20, 8, 22, 4, 12, 10, 14}
K1 = 3, K2 = 6
Output:
26

Explanation:
3rd smallest element is 10
6th smallest element is 20
Element between 10 and 20 
12,14. Their sum = 26.
 

Example 2:

Input
N = 6
A[] = {10, 2, 50, 12, 48, 13}
K1= 2, K2 = 6
Output:
73 
"""

import heapq


class Solution:
    def sumBetweenTwoKth(self, A, N, K1, K2):

        # k1 k2 is the smallest number

        def findKthSmallest(arr, k):
            max_heap = []

            for i in arr:
                heapq.heappush(max_heap, -1*i)

                if len(max_heap) > k:
                    heapq.heappop(max_heap)

            return -1*heapq.heappop(max_heap)

        min_val = findKthSmallest(A, K1)
        max_val = findKthSmallest(A, K2)

        res = 0

        for ele in A:
            if ele > min_val and ele < max_val:
                res += ele

        return res
