# https://leetcode.com/problems/recover-binary-search-tree/description/
""" 
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree 
were swapped by mistake. Recover the tree without changing its structure.


Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.


Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
"""


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        first = [None]
        middle = [None]
        last = [None]
        prev = [TreeNode(float('-inf'))]

        def inorder(root):

            if not root:
                return None

            inorder(root.left)

            # DO
            if prev[0] and prev[0].val > root.val:
                if first[0] == None:
                    first[0] = prev[0]
                    middle[0] = root
                else:
                    last[0] = root

            prev[0] = root
            inorder(root.right)

        inorder(root)

        if first[0] and last[0]:
            first[0].val, last[0].val = last[0].val, first[0].val
        else:
            first[0].val, middle[0].val = middle[0].val, first[0].val
