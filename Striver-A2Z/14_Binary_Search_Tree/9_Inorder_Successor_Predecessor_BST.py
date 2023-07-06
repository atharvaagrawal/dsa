# https://practice.geeksforgeeks.org/problems/predecessor-and-successor/1

""" 
There is BST given with the root node with the key part as an integer only. 
You need to find the in-order successor and predecessor of a given key. 
If either predecessor or successor is not found, then set it to NULL.

Note:- In an inorder traversal the number just smaller than the target is the predecessor 
and the number just greater than the target is the successor. 

Input:
        10
      /   \
     2    11
   /  \ 
  1    5
      /  \
     3    6
      \
       4
key = 8
Output: 
6 10
Explanation: 
In the given BST the inorder predecessor of 8 is 6 and inorder successor of 8 is 10.
"""


class Solution:
    def findPreSuc(self, root, pre, suc, key):

        # Number just smaller than the target - Predecessor
        # Number just greater than the target - Successor

        temp = root
        succ = None
        while temp:

            if key >= temp.key:
                temp = temp.right
            else:
                succ = temp
                temp = temp.left

        temp = root
        pree = None

        while temp:

            if key <= temp.key:
                temp = temp.left
            else:
                pree = temp
                temp = temp.right

        if succ:
            suc.key = succ.key
        if pree:
            pre.key = pree.key
