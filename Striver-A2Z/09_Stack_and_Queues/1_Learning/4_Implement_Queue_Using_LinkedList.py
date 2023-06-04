# https://practice.geeksforgeeks.org/problems/implement-queue-using-linked-list/1

""" 
Implement a Queue using Linked List. 
A Query Q is of 2 Types
(i) 1 x   (a query of this type means  pushing 'x' into the queue)
(ii) 2     (a query of this type means to pop an element from the queue and print the poped element)

Example 1:

Input:
Q = 5
Queries = 1 2 1 3 2 1 4 2
Output: 2 3
Explanation: n the first testcase
1 2 the queue will be {2}
1 3 the queue will be {2 3}
2   poped element will be 2 the
    queue will be {3}
1 4 the queue will be {3 4}
2   poped element will be 3.

Example 2:

Input:
Q = 4
Queries = 1 2 2 2 1 3 
Output: 2 -1
Explanation: In the second testcase 
1 2 the queue will be {2}
2   poped element will be {2} then
    the queue will be empty. 
2   the queue is empty and hence -1
1 3 the queue will be {3}.
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class MyQueue:
    def __init__(self):
        self.head = None
        self.end = None

    # Function to push an element into the queue.
    def push(self, item):
        newNode = Node(item)

        if self.head == None:
            self.head = newNode
            self.end = self.head
        else:
            self.end.next = newNode
            self.end = self.end.next

    # Function to pop front element from the queue.
    def pop(self):
        if not self.head:
            return -1
        else:
            data = self.head.data
            self.head = self.head.next

        return data
