# https://practice.geeksforgeeks.org/problems/delete-node-in-doubly-linked-list/1

""" 
Given a doubly linked list and a position. The task is to delete a node from given 
position in a doubly linked list.

Example 1:

Input:
LinkedList = 1 <--> 3 <--> 4 
x = 3
Output: 1 3  
Explanation: After deleting the node at
position 3 (position starts from 1),
the linked list will be now as 1->3.
"""


class Solution:
    def deleteNode(self, head, x):
        temp = head

        if x == 1:
            temp.next.prev = None
            head = temp.next
            return head

        c = 1
        while c != x:
            temp = temp.next
            c += 1

        # temp is the node to be deleted
        temp.prev.next = temp.next

        if temp.next:
            temp.next.prev = temp.prev

        return head
