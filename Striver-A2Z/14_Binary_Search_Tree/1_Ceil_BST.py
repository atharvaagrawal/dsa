# https://practice.geeksforgeeks.org/problems/implementing-ceil-in-bst/1


""" 
Given a BST and a number X, find Ceil of X.
Note: Ceil(X) is a number that is either equal to X or is immediately greater than X.

Example 1:

Input:
      5
    /   \
   1     7
    \
     2 
      \
       3
X = 3
Output: 3
Explanation: We find 3 in BST, so ceil
of 3 is 3.

Example 2:

Input:
     10
    /  \
   5    11
  / \ 
 4   7
      \
       8
X = 6
Output: 7
Explanation: We find 7 in BST, so ceil
of 6 is 7.
"""


class Solution:
    def findCeil(self, root, inp):
        # code here

        # Equal to X or immediate greater than X
        def solve(root, ceil):

            if not root:
                return ceil

            if inp > root.key:
                return solve(root.right, ceil)
            else:
                return solve(root.left, root.key)

        return solve(root, -1)
