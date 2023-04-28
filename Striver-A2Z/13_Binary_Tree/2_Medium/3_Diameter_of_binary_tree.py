""" 
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = []
        maxi.append(0)

        def height(r, maxi):
            if r is None:
                return 0

            cl = height(r.left, maxi)
            cr = height(r.right, maxi)

            maxi[0] = max(maxi[0], cl+cr)

            return 1+max(cl, cr)

        height(root, maxi)
        return maxi[0]
