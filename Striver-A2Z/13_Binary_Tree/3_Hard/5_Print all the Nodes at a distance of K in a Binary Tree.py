# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/

""" 
Given the root of a binary tree, the value of a target node target, and an integer k, 
return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order. 


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        # Steps:
        # 1. Create Map of Node and parent
        # 2. Find the target Node
        # 3. Using Queue and Visited Map find all the distance

        node_parent = dict()
        q = [root]

        # 1.
        def create_node_parent(root, parent):
            if not root:
                return None

            left = create_node_parent(root.left, root)
            right = create_node_parent(root.right, root)
            if parent:
                node_parent[root] = parent

            return root

        create_node_parent(root, None)

        # 2.
        # 3.

        queue = [target]
        visited = dict()
        dis = 0

        while queue:
            n = len(queue)

            if dis == k:
                break

            for i in range(n):
                node = queue.pop(0)

                if node in visited:
                    continue

                visited[node] = 1

                # Visit in all three direction
                if node.left and node.left not in visited:
                    queue.append(node.left)
                if node.right and node.right not in visited:
                    queue.append(node.right)

                if node in node_parent and node_parent[node] not in visited:
                    parent = node_parent[node]
                    queue.append(parent)
            dis += 1

        res = []
        for i in queue:
            res.append(i.val)

        return res
