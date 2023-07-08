# https://practice.geeksforgeeks.org/problems/unique-binary-tree-requirements/1

""" 
Geek wants to know the traversals required to construct a unique binary tree. 
Given a pair of traversal, return true if it is possible to construct unique binary tree 
from the given traversals otherwise return false.

Each traversal is represented with an integer: preorder - 1, inorder - 2, postorder - 3.   

Example 1:

Input:
a = 1, b=2
Output: 1
Explanation: We can construct binary tree using inorder traversal and preorder traversal. 

Example 2:

Input: a = 1, b=3
Output: 0 
Explanation: We cannot construct binary tree using preorder traversal and postorder traversal. 
"""


class Solution:
    def isPossible(self, a, b):

        # 1 - PreOrder
        # 2 - Inorder
        # 3 - PostOrder

        if a == b:
            return False

        if a == 2 or b == 2:
            return True

        return False
