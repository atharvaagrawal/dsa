# https://leetcode.com/problems/add-two-numbers/description/

""" 
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2

        # If any linklist is empty
        if temp1 == None and temp2 == None:
            return None
        if temp2 == None:
            return temp1
        if temp1 == None:
            return temp2

        # Calculating
        sum = 0
        carry = 0
        head = None

        head = ListNode()
        n = head

        while (temp1 or temp2 or carry != 0):
            if temp1 != None and temp2 != None:
                sum = temp1.val + temp2.val + carry
                temp1 = temp1.next
                temp2 = temp2.next
            elif temp1 != None:
                sum = temp1.val + carry
                temp1 = temp1.next
            elif temp2 != None:
                sum = temp2.val + carry
                temp2 = temp2.next
            else:
                sum = carry
                carry = 0
            temp3 = None

            if sum < 10:
                temp3 = ListNode(sum)
                carry = 0
            else:
                carry = sum//10
                temp3 = ListNode(sum % 10)

            n.next = temp3
            n = n.next

        return head.next


class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], c=0) -> Optional[ListNode]:

        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10)

        if (l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next, l2.next, c)
        return ret
