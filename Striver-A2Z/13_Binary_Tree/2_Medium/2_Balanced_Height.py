class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True
         
        def height(r):
            if r is None:
                return 0

            cl = 0
            cr = 0
            
            if r.left:
                cl = height(r.left)
            if r.right:
                cr = height(r.right)
            
            if cl == -1 or cr == -1:
                return -1
            
            if abs(cl-cr) > 1:
                return -1

            return 1+ max(cl,cr)
            

        return height(root) != -1