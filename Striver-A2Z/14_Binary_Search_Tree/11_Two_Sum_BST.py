
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/

""" 
Given the root of a binary search tree and an integer k, return true if there exist two elements 
in the BST such that their sum is equal to k, or false otherwise.

Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
 """

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack_increase = []

        self.stack_decrease = []

        temp = root

        while temp:
            self.stack_increase.append(temp)
            temp = temp.left

        while root:
            self.stack_decrease.append(root)
            root = root.right

    def next(self) -> int:
        if not self.stack_increase:
            return False

        node = self.stack_increase.pop()

        temp = node

        if temp.right:
            temp = temp.right
            self.stack_increase.append(temp)
        else:
            return node

        temp = temp.left

        while temp:
            self.stack_increase.append(temp)
            temp = temp.left

        return node

    def before(self) -> int:
        if not self.stack_decrease:
            return False

        node = self.stack_decrease.pop()

        temp = node

        if temp.left:
            temp = temp.left
            self.stack_decrease.append(temp)
        else:
            return node

        temp = temp.right

        while temp:
            self.stack_decrease.append(temp)
            temp = temp.right

        return node


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        # Create BST InOrder Iterator
        itr = BSTIterator(root)

        i = itr.next()
        j = itr.before()

        while i != j:
            if i.val + j.val == k:
                return True

            if i.val + j.val < k:
                i = itr.next()
            else:
                j = itr.before()

            if i == False or j == False:
                return False

        return False
