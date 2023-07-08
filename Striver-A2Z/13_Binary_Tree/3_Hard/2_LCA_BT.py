# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

""" 
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as 
the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
 """

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # Two Cases:
        # 1: both will on same direction
        # 2: both will on different direction
        def solve(root):
            if not root:
                return None

            # If found any one node
            if root.val == p.val or root.val == q.val:
                return root

            left = solve(root.left)
            right = solve(root.right)

            if left == None:
                return right
            elif right == None:
                return left
            else:
                return root

        return solve(root)
