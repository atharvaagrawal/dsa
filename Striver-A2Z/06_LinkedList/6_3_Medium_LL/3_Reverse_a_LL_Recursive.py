# https://leetcode.com/problems/reverse-linked-list/description/

""" 
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Recursive

        if not head:
            return head

        def solve(temp):

            if not temp.next or not temp:
                return temp

            h2 = solve(temp.next)

            temp.next.next = temp
            temp.next = None

            return h2

        return solve(head)
