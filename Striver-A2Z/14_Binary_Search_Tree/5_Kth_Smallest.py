# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # Inorder of BST is sorted

        def inorder(root, k):
            if not root:
                return None

            left = inorder(root.left, k)
            if left:
                return left

            k[0] -= 1
            if k[0] == 0:
                return root

            return inorder(root.right, k)
        k = [k]
        node = inorder(root, k)

        return node.val
