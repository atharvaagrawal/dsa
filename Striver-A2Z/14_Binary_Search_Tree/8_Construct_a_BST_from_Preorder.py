# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/

""" 
Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), 
construct the tree and return its root.

It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly 
less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, 
then traverses Node.right.

Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

"""


from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# BruteForce
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        def construct(root, val):
            if not root:
                return TreeNode(val)

            if val > root.val:
                root.right = construct(root.right, val)
                return root
            elif val < root.val:
                root.left = construct(root.left, val)
                return root

        root = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            construct(root, preorder[i])

        return root


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        root = TreeNode(preorder[0])
        upper_bound = float('inf')

        def build(ind, upper_bound):

            if ind[0] == len(preorder) or preorder[ind[0]] > upper_bound:
                return None

            root = TreeNode(preorder[ind[0]])
            ind[0] += 1

            root.left = build(ind, root.val)
            root.right = build(ind, upper_bound)
            return root

        ind = [0]
        return build(ind, upper_bound)
