# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
""" 
You are given the root node of a binary search tree (BST) and a value to insert into the tree.
Return the root node of the BST after the insertion. It is guaranteed that the new value does 
not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains 
a BST after insertion. You can return any of them.

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def solve(root):

            if root.left is None and val < root.val:
                root.left = TreeNode(val)
                return
            elif root.right is None and val > root.val:
                root.right = TreeNode(val)
                return

            if val > root.val:
                return solve(root.right)
            else:
                return solve(root.left)

        if not root:
            return TreeNode(val)

        solve(root)

        return root
