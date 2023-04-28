""" 
https://leetcode.com/problems/maximum-width-of-binary-tree/

Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), 
where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also 
counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.
"""

from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Using Level Order Traversal
        queue = []
        queue.append([root, 0])
        res = 0

        while len(queue) > 0:
            n = len(queue)
            mmin = queue[0][1]
            first = last = 0

            # print("\n He",mmin)
            # for i,j in queue:
            #     print(i.val,j,end=" ")

            for i in range(n):
                temp = queue.pop(0)

                # print(temp[0].val,temp[1])

                cur_id = temp[1] - mmin
                temp = temp[0]
                if i == 0:
                    first = cur_id
                if i == n-1:
                    last = cur_id
                if temp.left:
                    queue.append([temp.left, cur_id*2+1])
                if temp.right:
                    queue.append([temp.right, cur_id*2+2])

            res = max(res, last-first+1)

        return res
