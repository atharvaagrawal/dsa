# https://practice.geeksforgeeks.org/problems/find-length-of-loop/1

""" 
Given a linked list of size N. The task is to complete the function countNodesinLoop() 
that checks whether a given Linked List contains a loop or not and if the loop is present
then return the count of nodes in a loop or else return 0. C is the position of the node 
to which the last node is connected. If it is 0 then no loop.

Input:
N = 10
value[]={25,14,19,33,10,21,39,90,58,45}
C = 4
Output: 7
Explanation: The loop is 45->33. So
length of loop is 33->10->21->39->
90->58->45 = 7. The number 33 is
connected to the last node to form the
loop because according to the input the
4th node from the beginning(1 based
index) will be connected to the last
node for the loop.
"""


def countNodesinLoop(head):

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            entry = head
            while slow != entry:
                slow = slow.next
                entry = entry.next

            # Now calculate the total Nodes
            count = 1
            slow = slow.next
            while slow != entry:
                slow = slow.next
                count += 1
            return count

    return 0
