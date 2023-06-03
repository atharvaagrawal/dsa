# https://leetcode.com/problems/sort-list/description/

""" 
Given the head of a linked list, return the list after sorting it in ascending order.

Input: head = [4,2,1,3]
Output: [1,2,3,4]
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def getMiddle(head):
            slow = head
            fast = head.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        def merge(left, right):
            tail = dummy = ListNode()

            while left and right:
                if left.val < right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next

            if left:
                tail.next = left
            if right:
                tail.next = right

            return dummy.next

        # Applying Merge Sort
        def mergeSort(head):
            if not head or not head.next:
                return head

            # Split the list into two halfs
            left = head
            right = getMiddle(head)

            temp = right.next
            right.next = None
            right = temp

            left = mergeSort(left)
            right = mergeSort(right)

            return merge(left, right)

        return mergeSort(head)
