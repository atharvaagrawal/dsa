# https://practice.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1

""" 
Given a doubly linked list of n elements. The task is to reverse the doubly linked list.

Example 1:

Input:
LinkedList: 3 <--> 4 <--> 5
Output: 5 4 3

Example 2:
Input:
LinkedList: 75 <--> 122 <--> 59 <--> 196
Output: 196 59 122 75
"""


def reverseDLL(head):
    # return head after reversing

    temp = head

    while temp.next:
        swap = temp.prev

        temp.prev = temp.next
        temp.next = swap

        temp = temp.prev

    temp.next = temp.prev
    temp.prev = None

    head = temp

    return head
