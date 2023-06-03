# https://practice.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1

""" 
A number N is represented in Linked List such that each digit corresponds to a node in linked list. 
You need to add 1 to it.

Example 1:

Input:
LinkedList: 4->5->6
Output: 457 

Example 2:

Input:
LinkedList: 1->2->3
Output: 124 
"""

import sys
sys.setrecursionlimit(10 ** 9)


class Solution:
    def addOne(self, head):

        if not head:
            return head

        def solve(head):
            if not head.next:
                num = head.data + 1
                carry = 0
                if num >= 10:
                    carry = num//10
                    num = num % 10

                head.data = num
                return carry

            carryr = solve(head.next)

            if carryr == 0:
                return 0
            else:
                num = head.data + carryr

                if num >= 10:
                    carryr = num//10
                    num = num % 10
                else:
                    carryr = 0
                head.data = num

                return carryr

        carry = solve(head)

        if carry > 0:
            newNode = Node(carry)
            newNode.next = head
            head = newNode

        return head


class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next


def PrintList(head):
    while head:
        print(head.data, end=" ")
        head = head.next


num = "59703500570331375262662556488617535371687193415340170536352797941799549209385189189519436387287108813079124725453582402760679640100258623696628437950510482299676079665621648382018688729928795374257938904748868174606279240661480942609656337027418759575056996876876141386665270893934401634280740237765759921556618646399302209068266372968423964367102738443239116504635130359999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999"

# num = "456"

ll = LinkedList()

for digit in num:
    ll.insert(int(digit))


resHead = Solution().addOne(ll.head)
PrintList(resHead)
