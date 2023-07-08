# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        # Inorder Map Created
        inMap = dict()
        for i in range(len(inorder)):
            inMap[inorder[i]] = i

        def build(postStart, postEnd, inStart, inEnd):
            if postStart > postEnd or inStart > inEnd:
                return None

            root = TreeNode(postorder[postEnd])

            inRoot = inMap[root.val]
            numsLeft = inRoot - inStart

            root.left = build(postStart, postStart +
                              numsLeft-1, inStart, inRoot-1)

            root.right = build(postStart+numsLeft, postEnd-1, inRoot+1, inEnd)

            return root

        return build(0, len(postorder)-1, 0, len(inorder)-1)
