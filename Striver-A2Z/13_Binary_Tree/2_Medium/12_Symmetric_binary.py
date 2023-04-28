# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
""" 
https://takeuforward.org/data-structure/check-for-symmetrical-binary-tree/

Intuition: We need to understand the property of the mirror. We can ignore the root node as it is 
lying on the mirror line. In the next level, for a symmetric tree, the node at the root’s left 
should be equal to the node at the root’s right.

If we take two variables root1 and root2 to represent the left child of root and right child of the root, 
then 
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # We can take 2 variable

        def solve(root1, root2):
            if not root1 or not root2:
                return root1 == root2

            if root1.val == root2.val:
                return solve(root1.left, root2.right) and solve(root1.right, root2.left)
            return False

        return solve(root.left, root.right)
