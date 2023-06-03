# https://practice.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1
""" 
Given a linked list of N nodes where nodes can contain values 0s, 1s, and 2s only. The task is to segregate 0s, 1s, and 2s linked list such that all zeros segregate to head side, 2s at the end of the linked list, and 1s in the mid of 0s and 2s.

Example 1:

Input:
N = 8
value[] = {1,2,2,1,2,0,2,2}
Output: 0 1 1 2 2 2 2 2
Explanation: All the 0s are segregated
to the left end of the linked list,
2s to the right end of the list, and
1s in between.

Example 2:

Input:
N = 4
value[] = {2,2,0,1}
Output: 0 1 2 2
Explanation: After arranging all the
0s,1s and 2s in the given format,
the output will be 0 1 2 2.
"""


class Solution:
    # Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):

        zero = 0
        one = 0
        two = 0

        temp = head

        while temp:
            if temp.data == 0:
                zero += 1
            elif temp.data == 1:
                one += 1
            elif temp.data == 2:
                two += 1
            temp = temp.next

        temp = head

        # firt zero
        while zero:
            temp.data = 0
            zero -= 1
            temp = temp.next

        # then 1
        while one:
            temp.data = 1
            one -= 1
            temp = temp.next

        # then 2
        while two:
            temp.data = 2
            two -= 1
            temp = temp.next

        return head
