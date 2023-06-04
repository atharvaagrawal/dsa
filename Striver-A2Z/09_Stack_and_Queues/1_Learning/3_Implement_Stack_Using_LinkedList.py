# https://practice.geeksforgeeks.org/problems/implement-stack-using-linked-list/1
""" 
Let's give it a try! You have a linked list and you have to implement the functionalities 
push and pop of stack using this given linked list. Your task is to use the class as shown 
in the comments in the code editor and complete the functions push() and pop() to implement a stack. 

Example 1:

Input: 
push(2)
push(3)
pop()
push(4) 
pop()
Output: 3 4
Explanation: 
push(2)    the stack will be {2}
push(3)    the stack will be {2 3}
pop()      poped element will be 3,
           the stack will be {2}
push(4)    the stack will be {2 4}
pop()      poped element will be 4
Example 2:

Input: 
pop()
push(4)
push(5)
pop()
Output: -1 5
"""


class StackNode:
    # Constructor to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None


class MyStack:
    def __init__(self):
        self.top = None

    # Function to push an integer into the stack.
    def push(self, data):
        newNode = StackNode(data)

        if self.top == None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode

    # Function to remove an item from top of the stack.

    def pop(self):
        if self.top == None:
            return -1
        else:
            data = self.top.data
            self.top = self.top.next

        return data
