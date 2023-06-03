# https://practice.geeksforgeeks.org/problems/insert-a-node-in-doubly-linked-list/1

""" 
Given a doubly-linked list, a position p, and an integer x. 
The task is to add a new node with value x at the position 
just after pth node in the doubly linked list.

Input:
LinkedList: 2<->4<->5
p = 2, x = 6 
Output: 2 4 5 6
Explanation: p = 2, and x = 6. So, 6 is
inserted after p, i.e, at position 3
(0-based indexing).
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def addNode(head, p, data):
    # Code here
    newNode = Node(data)

    if not head:
        head = newNode
        return head

    temp = head

    c = 0
    while c != p:
        temp = temp.next
        c += 1

    newNode.next = temp.next
    temp.next = newNode
    newNode.prev = temp

    if newNode.next:
        newNode.next.prev = newNode

    return head
