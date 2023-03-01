# https://takeuforward.org/binary-tree/binary-tree-traversal-inorder-preorder-postorder/

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []

        queue = []

        temp = root
        queue.append(root)
        
        res = []

        while len(queue) > 0:
            n = len(queue)
            l = []
            for i in range(n):
                temp = queue.pop(0)
                
                if temp == None:
                    break

                if temp.left != None:
                    queue.append(temp.left)
                if temp.right != None:
                    queue.append(temp.right)

                l.append(temp.val)
            
            res.append(l)
        
        return res
        