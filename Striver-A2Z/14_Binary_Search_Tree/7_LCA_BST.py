# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/


""" 
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes 
p and q as the lowest node in T that has both p and q as descendants (where we allow a node to
be a descendant of itself).”

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def solve(root, p, q):

            if not root:
                return

            if p.val > root.val and q.val < root.val:
                return root
            elif p.val < root.val and q.val > root.val:
                return root
            elif root.val == q.val or root.val == p.val:
                return root

            if p.val < root.val and q.val < root.val:
                return solve(root.left, p, q)
            else:
                return solve(root.right, p, q)

        return solve(root, p, q)
