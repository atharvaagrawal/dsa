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
        temp = head
        if not head:
            return head

        prev = temp
        temp = temp.next
        prev.next = None
        if not temp:
            return head
        while temp.next:
            t1 = temp.next
            temp.next = prev
            prev = temp
            temp = t1
        temp.next = prev

        return temp
