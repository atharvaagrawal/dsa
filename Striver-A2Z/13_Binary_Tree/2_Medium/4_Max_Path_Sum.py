# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.msum = float('-inf')
        print(self.msum)
        self.get_sum(root)
        return self.msum
    
    def get_sum(self, node):
        if not node:
            return 0
        
        ls = self.get_sum(node.left)
        rs = self.get_sum(node.right)
        
        max_single_path = max(node.val+max(ls,rs), node.val)
        self.msum = max(self.msum, max_single_path , node.val+ls+rs)
        print(ls,rs,node.val,self.msum)
        return max_single_path