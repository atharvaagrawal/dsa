# https://www.interviewbit.com/problems/path-to-given-node/
""" 
You need to find the path from Root to a given node B.

NOTE:
No two nodes in the tree have same data values.
You can assume that B is present in the tree A and a path always exists.
"""


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        res = []

        def inorder(root):
            if not root:
                return False

            if root:
                res.append(root.val)

                if root.val == B:
                    return True

                res1 = inorder(root.left)
                res2 = inorder(root.right)

                if res1 or res2:
                    return True

                res.pop()
                return False

        inorder(A)

        return res
