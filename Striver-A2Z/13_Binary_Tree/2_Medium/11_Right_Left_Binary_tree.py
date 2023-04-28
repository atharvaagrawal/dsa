""" 

Given the root of a binary tree, imagine yourself standing on the right side of it, return the 
values of the nodes you can see ordered from top to bottom.

"""


# First thought: Take right boundary and count the level and if left level exceeds the right level,
# then that many nodes will also be visible.

# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

#         # In this we will able to see the right view till the level
#         # After that left side
#         if root is None:
#             return []

#         right_view = []
#         temp = root
#         level = 0
#         while temp:
#             right_view.append(temp.val)
#             level += 1
#             if temp.right:
#                 temp = temp.right
#             else:
#                 temp = temp.left
#         print(level)

#         # Find left level
#         if root.left:
#             temp = root.left
#         else:
#             return right_view

#         left_level = 0
#         while temp:
#             left_level += 1
#             if left_level >= level:
#                 right_view.append(temp.val)
#             if temp.right:
#                 temp = temp.right
#             else:
#                 temp = temp.left
#         print(left_level)
#         return right_view

from typing import Optional, List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Intuition: We have to do a Recursive Level Order Traversal.
# Root Right Left     —-> for Right view

# Root Left Right     —–> for Left view
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Level Order Traversal
        # Root -> Right -> Left

        if not root:
            return []

        queue = []

        queue.append(root)
        res = []

        while len(queue) > 0:
            n = len(queue)
            flag = 1

            for i in range(n):
                temp = queue.pop(0)
                if temp == None:
                    break
                if flag:
                    res.append(temp.val)
                    flag = 0

                if temp.right:
                    queue.append(temp.right)

                if temp.left:
                    queue.append(temp.left)
        return res
