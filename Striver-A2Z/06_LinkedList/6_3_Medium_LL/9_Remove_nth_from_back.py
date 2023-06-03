# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

""" 
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

"""
from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Optimal: TC = O(n)
class Solution1:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        start = ListNode()
        start.next = head

        slow = start
        fast = start
        c = n

        # Place fast to the nth position from start
        while c:
            fast = fast.next
            c -= 1

        # Now Move both fast and slow by 1
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return start.next


# BruteForce TC = O(n)+O(n)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        # count the nodes and remove the nth from last
        count = 0
        temp = head

        while temp:
            temp = temp.next
            count += 1

        print(count)

        # Now Remove the nth node
        nth = count - n

        if nth == 0:
            head = head.next
            return head

        temp = head
        count = 0
        while count != nth-1 and temp:
            count += 1
            temp = temp.next

        if not temp:
            return None

        if temp.next:
            temp.next = temp.next.next
        else:
            temp.next = None

        return head
