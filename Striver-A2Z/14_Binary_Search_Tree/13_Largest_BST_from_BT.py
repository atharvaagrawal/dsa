# https://practice.geeksforgeeks.org/problems/largest-bst/1
""" 
Given a binary tree. Find the size of its largest subtree that is a Binary Search Tree.
Note: Here Size is equal to the number of nodes in the subtree.


Example 1:

Input:
        1
      /   \
     4     4
   /   \
  6     8
Output: 1
Explanation: There's no sub-tree with size
greater than 1 which forms a BST. All the
leaf Nodes are the BSTs with size equal
to 1.

Example 2:

Input: 6 6 3 N 2 9 3 N 8 8 2
            6
        /       \
       6         3
        \      /   \
         2    9     3
          \  /  \
          8 8    2 
Output: 2
Explanation: The following sub-tree is a
BST of size 2: 
       2
    /    \ 
   N      8
"""


class NodeValue:
    def __init__(self, minNode, maxNode, maxSize):

        self.minNode = minNode
        self.maxNode = maxNode
        self.maxSize = maxSize


class Solution:
    # Return the size of the largest sub-tree which is also a BST
    def largestBst(self, root):

        def solve(root):
            if not root:
                return NodeValue(float('inf'), float('-inf'), 0)

            left = solve(root.left)
            right = solve(root.right)

            if left.maxNode < root.data and root.data < right.minNode:

                return NodeValue(min(root.data, left.minNode), max(root.data, right.maxNode), left.maxSize+right.maxSize+1)

            return NodeValue(float('-inf'), float('inf'), max(left.maxSize, right.maxSize))

        res = solve(root)

        return res.maxSize
