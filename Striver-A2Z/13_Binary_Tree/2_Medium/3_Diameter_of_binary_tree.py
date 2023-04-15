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
        def height(r,maxi):
            if r is None:
                return 0
        
            cl = height(r.left,maxi)
            cr = height(r.right,maxi)

            maxi[0] = max(maxi[0],cl+cr)

            return 1+max(cl,cr)
        
        height(root,maxi)
        return maxi[0]