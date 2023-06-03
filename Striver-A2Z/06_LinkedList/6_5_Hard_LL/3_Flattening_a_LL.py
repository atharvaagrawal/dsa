# https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1
""" 
Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:
(i) a next pointer to the next node,
(ii) a bottom pointer to a linked list where this node is head.
Each of the sub-linked-list is in sorted order.
Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. 

Note: The flattened list will be printed using the bottom pointer instead of the next pointer.
For more clarity have a look at the printList() function in the driver code.

 

Example 1:

Input:
5 -> 10 -> 19 -> 28
|     |     |     | 
7     20    22   35
|           |     | 
8          50    40
|                 | 
30               45
Output:  5-> 7-> 8- > 10 -> 19-> 20->
22-> 28-> 30-> 35-> 40-> 45-> 50.
Explanation:
The resultant linked lists has every 
node in a single level.
(Note: | represents the bottom pointer.)
 

Example 2:

Input:
5 -> 10 -> 19 -> 28
|          |                
7          22   
|          |                 
8          50 
|                           
30              
Output: 5->7->8->10->19->22->28->30->50
Explanation:
The resultant linked lists has every
node in a single level.

(Note: | represents the bottom pointer.)
"""


class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None


def mergeTwoLists(a, b):
    temp = Node(0)
    res = temp
    while a != None and b != None:
        if a.data < b.data:
            temp.bottom = a
            temp = temp.bottom
            a = a.bottom
        else:
            temp.bottom = b
            temp = temp.bottom
            b = b.bottom
    if a:
        temp.bottom = a
    else:
        temp.bottom = b
    return res.bottom


def flatten(root):
    if root == None or root.next == None:
        return root
    # recur for list on right
    root.next = flatten(root.next)

    # now merge
    root = mergeTwoLists(root, root.next)

    # return the root
    # it will be in turn merged with its left
    return root
