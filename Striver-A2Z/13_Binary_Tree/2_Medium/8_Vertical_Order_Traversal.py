""" 
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.
"""

import heapq
from collections import deque, defaultdict
from typing import List


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Vertical, Level
        res = []

        # Level Order Traversal
        def solve(root):
            d = {}

            # v = Verticals  l = Level
            queue = [(root, 0, 0)]

            while queue:
                root, v, l = queue.pop(0)

                if v not in d:
                    d[v] = {}

                if l not in d[v]:
                    d[v][l] = []

                d[v][l].append(root.val)

                if root.left:
                    queue.append((root.left, v-1, l+1))
                if root.right:
                    queue.append((root.right, v+1, l+1))

            for v in sorted(d.keys()):
                col = []
                for l in sorted(d[v].keys()):
                    col.extend(sorted(d[v][l]))
                res.append(col)

            return res

        return solve(root)


# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None


def findVertical(root: Node) -> List[List[int]]:
    nodes = defaultdict(lambda: defaultdict(list))
    print(nodes)
    q = deque([(root, 0, 0)])
    while q:
        curr, x, y = q.popleft()
        nodes[x][y].append(curr.data)
        print(nodes)
        if curr.left:
            q.append((curr.left, x-1, y+1))
        if curr.right:
            q.append((curr.right, x+1, y+1))
    ans = []
    for x in sorted(nodes.keys()):
        col = []
        for y in sorted(nodes[x].keys()):
            col.extend(sorted(nodes[x][y]))
        ans.append(col)
    return ans


# root = Node(1)
# root.left = Node(2)
# root.left.left = Node(4)
# root.left.right = Node(10)
# root.left.left.right = Node(5)
# root.left.left.right.right = Node(6)
# root.right = Node(3)
# root.right.left = Node(9)
# root.right.right = Node(10)

# verticalTraversal = findVertical(root)
# print("The Vertical Traversal is : ")
# for vertical in verticalTraversal:
#     print(*vertical)
