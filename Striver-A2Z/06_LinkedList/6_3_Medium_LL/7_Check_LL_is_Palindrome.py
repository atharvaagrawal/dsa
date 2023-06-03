# https://takeuforward.org/data-structure/check-if-given-linked-list-is-plaindrome/
# https://leetcode.com/problems/palindrome-linked-list/


""" 
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

Input: head = [1,2,2,1]
Output: true 
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        # Find the Middle of LL
        slow = head
        fast = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        middle = slow

        # Reverse the LL from slow.next till end
        ptr = slow.next
        pre = None
        nex = None

        while ptr != None:
            nex = ptr.next
            ptr.next = pre
            pre = ptr
            ptr = nex

        slow.next = pre

        # Now check
        temp = head
        middle = middle.next
        while middle:
            if temp.val != middle.val:
                return False
            temp = temp.next
            middle = middle.next

        return True
