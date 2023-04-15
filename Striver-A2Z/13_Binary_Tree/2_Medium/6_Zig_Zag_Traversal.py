# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []        
        queue = []
        
        flag = 0  # 0 - Zig(left to right) 1-Zag(right to left)
        
        queue.append(root)
        
        temp = root

        while len(queue) > 0:
            n = len(queue)
            l = []

            for i in range(n):
                temp = queue.pop(0)

                if temp == None:
                    break

                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                
                l.append(temp.val)
            
            if flag == 0:
                flag = 1
            else:
                flag = 0
                l.reverse()
                    
            res.append(l)
        
        return res

            
            
            
