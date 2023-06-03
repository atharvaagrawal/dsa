# https://practice.geeksforgeeks.org/problems/linked-list-insertion-1587115620/0

""" 
Create a link list of size N according to the given input literals. Each integer 
input is accompanied by an indicator which can either be 0 or 1. If it is 0, insert 
the integer in the beginning of the link list. If it is 1, insert the integer at the end of the link list. 
Hint: When inserting at the end, make sure that you handle NULL explicitly.

Example 1:

Input:
LinkedList: 9->0->5->1->6->1->2->0->5->0
Output: 5 2 9 5 6
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:

    def insertAtBegining(self, head, x):
        newNode = Node(x)
        newNode.next = head
        head = newNode
        return head

    def insertAtEnd(self, head, x):
        newNode = Node(x)

        if not head:
            head = newNode
            return head

        temp = head

        while temp.next:
            temp = temp.next

        temp.next = newNode

        return head
