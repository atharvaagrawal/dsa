# https://practice.geeksforgeeks.org/problems/burning-tree/1
""" 
Given a binary tree and a node data called target. 
Find the minimum time required to burn the complete binary tree if the target is set on fire. 
It is known that in 1 second all nodes connected to a given node get burned. 
That is its left child, right child, and parent.


Note: The tree contains unique values.

Input:      
          1
        /   \
      2      3
    /  \      \
   4    5      6
       / \      \
      7   8      9
                   \
                   10
Target Node = 8
Output: 7
Explanation: If leaf with the value 
8 is set on fire. 
After 1 sec: 5 is set on fire.
After 2 sec: 2, 7 are set to fire.
After 3 sec: 4, 1 are set to fire.
After 4 sec: 3 is set to fire.
After 5 sec: 6 is set to fire.
After 6 sec: 9 is set to fire.
After 7 sec: 10 is set to fire.
It takes 7s to burn the complete tree.
"""


class Solution:
    def minTime(self, root, target):
        # code here

        # Step 1 Find the target node
        def find(root):

            if not root:
                return None

            if root.data == target:
                return root

            left = find(root.left)
            if left:
                return left
            right = find(root.right)
            if right:
                return right

            return None

        target = find(root)

        if not target:
            return 0

        # Step 2 Create Node Parent Map
        node_parent = dict()

        def create_node_parent(root, parent):
            if not root:
                return None

            create_node_parent(root.left, root)
            create_node_parent(root.right, root)

            if parent:
                node_parent[root] = parent

            return None

        create_node_parent(root, None)

        # Step 3: Calculate the time
        time = 0
        visited = dict()
        queue = [target]

        while queue:
            n = len(queue)

            fl = 0

            for _ in range(n):
                node = queue.pop(0)

                if node in visited:
                    return None

                visited[node] = 1

                if node.left and node.left not in visited:
                    fl = 1
                    queue.append(node.left)

                if node.right and node.right not in visited:
                    fl = 1
                    queue.append(node.right)

                if node in node_parent and node_parent[node] not in visited:
                    fl = 1
                    queue.append(node_parent[node])

            if fl:
                time += 1

        return time
