# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

""" 
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to 
the next node in the list and the left child pointer is always null.

The "linked list" should be in the same order as a pre-order traversal of the binary tree.


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
"""


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = [None]
        # PreOrder Traversal

        def flatten(root):
            if not root:
                return

            flatten(root.right)
            flatten(root.left)

            root.right = prev[0]
            root.left = None
            prev[0] = root

        flatten(root)
