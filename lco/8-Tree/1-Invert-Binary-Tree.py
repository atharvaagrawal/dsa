# https://leetcode.com/problems/invert-binary-tree/description/

from typing import Optional


""" 
Given the root of a binary tree, invert the tree, and return its root.

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def solve(root):
            if not root:
                return None

            left = solve(root.left)
            right = solve(root.right)

            root.right = left
            root.left = right
            return root

        solve(root)

        return root
