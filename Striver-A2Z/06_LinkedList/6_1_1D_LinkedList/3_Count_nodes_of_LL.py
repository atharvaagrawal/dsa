# https://practice.geeksforgeeks.org/problems/count-nodes-of-linked-list/0

""" 
Given a singly linked list. The task is to find the length of the linked list, 
where length is defined as the number of nodes in the linked list.

Example 1:

Input:
LinkedList: 1->2->3->4->5
Output: 5
Explanation: Count of nodes in the 
linked list is 5, which is its length.

Example 2:

Input:
LinkedList: 2->4->6->7->5->1->0
Output: 7
Explanation: Count of nodes in the
linked list is 7. Hence, the output
is 7.

"""


class Solution:

    # Function to count nodes of a linked list.
    def getCount(self, head_node):

        c = 0
        temp = head_node
        while temp:
            c += 1
            temp = temp.next

        return c
