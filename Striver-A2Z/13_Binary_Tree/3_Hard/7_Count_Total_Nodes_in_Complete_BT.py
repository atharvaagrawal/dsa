# https://leetcode.com/problems/count-complete-tree-nodes/description/
""" 
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in 
a complete binary tree, and all nodes in the last level are as far left as possible. 
It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.


Input: root = [1,2,3,4,5,6]
Output: 6
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left == None and root.right == None:
            return 1

        def getLeftHeight(root):
            if not root:
                return 0
            if root.left:
                return 1+getLeftHeight(root.left)
            return 1

        def getRightHeight(root):
            if not root:
                return 0
            if root.right:
                return 1+getRightHeight(root.right)
            return 1

        def solve(root):
            if not root:
                return 0

            left_height = getLeftHeight(root)
            right_height = getRightHeight(root)

            if left_height == right_height:
                return 2**right_height-1
            else:
                return 1+solve(root.left)+solve(root.right)

        return solve(root)
