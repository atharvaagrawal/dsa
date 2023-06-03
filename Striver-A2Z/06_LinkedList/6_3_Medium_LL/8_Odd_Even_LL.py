# https://leetcode.com/problems/odd-even-linked-list/

""" 
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        even_head = head.next
        odd_head = head

        even_start = head.next

        while odd_head and even_head and odd_head.next and even_head.next:

            odd_head.next = odd_head.next.next
            even_head.next = even_head.next.next

            odd_head = odd_head.next
            even_head = even_head.next

        odd_head.next = even_start

        return head
