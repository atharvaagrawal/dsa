# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def solve(r):
            if r:
                cl = 0
                cr = 0

                if r.left:
                    cl = 1 + solve(r.left)
                if r.right:
                    cr = 1 + solve(r.right)
                
                return max(cl,cr)

            return 0
        
        return solve(root)+1