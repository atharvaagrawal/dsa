# https://practice.geeksforgeeks.org/problems/children-sum-parent/1
""" 
Given a Binary Tree. Check whether all of its nodes have the value equal to the sum of their child nodes.

Example 1:

Input:
     10
    /
  10 
Output: 1
Explanation: Here, every node is sum of
its left and right child.


Example 2:

Input:
       1
     /   \
    4     3
   /  \
  5    N
Output: 0
Explanation: Here, 1 is the root node
and 4, 3 are its child nodes. 4 + 3 =
7 which is not equal to the value of
root node. Hence, this tree does not
satisfy the given conditions.
"""


class Solution:
    # Function to check whether all nodes of a tree have the value
    # equal to the sum of their child nodes.
    def isSumProperty(self, root):
        # code here

        def solve(root):
            if not root:
                return 0

            if root.left == None and root.right == None:
                return root.data

            left = solve(root.left)
            right = solve(root.right)

            if left == False and type(left) == type(False):
                return False

            if right == False and type(right) == type(False):
                return False

            if root.data != left+right:
                return False

            return root.data

        res = solve(root)

        if res == False:
            return 0

        return 1
