# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
""" 
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree 
and inorder is the inorder traversal of the same tree, construct and return the binary tree


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inMap = dict()
        for i in range(len(inorder)):
            inMap[inorder[i]] = i

        def build(preStart, preEnd, inStart, inEnd, inMap):

            if preStart > preEnd or inStart > inEnd:
                return None

            root = TreeNode(preorder[preStart])

            # Found the inorder position
            inRoot = inMap[root.val]
            numsLeft = inRoot - inStart

            root.left = build(preStart+1, preStart+numsLeft,
                              inStart, inRoot-1, inMap)

            root.right = build(preStart+1+numsLeft, preEnd,
                               inRoot+1, inEnd, inMap)

            return root

        return build(0, len(preorder)-1, 0, len(inorder)-1, inMap)
