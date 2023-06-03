# https://leetcode.com/problems/intersection-of-two-linked-lists/description/

""" 
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
 If the two linked lists have no intersection at all, return null.


The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB 
to your program. If you correctly return the intersected node, then your solution will be accepted.


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes 
before the intersected node in A; There are 3 nodes before the intersected node in B.
- Note that the intersected node's value is not 1 because the nodes with value 1 in A and B 
(2nd node in A and 3rd node in B) are different node references. In other words, they point to two different 
locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) 
point to the same location in memory.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        if not headA or not headB:
            return None

        temp1 = headA
        temp2 = headB

        while temp1 != temp2:
            temp1 = headB if temp1 == None else temp1.next
            temp2 = headA if temp2 == None else temp2.next

        return temp1
