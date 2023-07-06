# https://leetcode.com/problems/delete-node-in-a-bst/description/
""" 
Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMin(self, root):
        if root.left == None:
            return root
        return self.findMin(root.left)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if (root == None):
            # Element Not Found
            return None

        if (key > root.val):
            root.right = self.deleteNode(root.right, key)
            return root

        if (key < root.val):
            root.left = self.deleteNode(root.left, key)
            return root

        # leaf node
        if (root.left == None and root.right == None):
            del root
            return None

        # Node with 1 child
        if (root.left == None):
            temp = root.right
            del root
            return temp

        if (root.right == None):
            temp = root.left
            del root
            return temp

        # Node with 2 Child
        temp = self.findMin(root.right)
        root.val = temp.val

        root.right = self.deleteNode(root.right, temp.val)
        return root
