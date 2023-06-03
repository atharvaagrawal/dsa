# https://practice.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1
""" 
Given a sorted doubly linked list of positive distinct elements, the task is to find pairs in a 
doubly-linked list whose sum is equal to given value target. 

Example 1:

Input:  
1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9
target = 7
Output: (1, 6), (2,5)
Explanation: We can see that there are two pairs 
(1, 6) and (2,5) with sum 7.
"""

from typing import Optional


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None


class Solution:
    def findPairsWithGivenSum(self, target: int, head: Optional['Node']) -> List[List[int]]:
        # code here
        res = []

        if not head:
            return res

        left = head
        right = head

        while right.next:
            right = right.next

        while right.data > left.data:
            num = right.data+left.data
            if num == target:
                res.append([left.data, right.data])

            if num > target:
                right = right.prev
            else:
                left = left.next

        return res
