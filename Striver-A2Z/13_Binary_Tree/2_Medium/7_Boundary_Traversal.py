""" 
Given a Binary Tree, find its Boundary Traversal. The traversal should be in the following order: 

Left boundary nodes: defined as the path from the root to the left-most node ie- the leaf node you could reach when you always travel preferring the left subtree over the right subtree. 
Leaf nodes: All the leaf nodes except for the ones that are part of left or right boundary.
Reverse right boundary nodes: defined as the path from the right-most node to the root. The right-most node is the leaf node you could reach when you always travel preferring the right subtree over the left subtree. Exclude the root from this as it was already included in the traversal of left boundary nodes.
Note: If the root doesn't have a left subtree or right subtree, then the root itself is the left or right boundary. 

"""


class Solution:
    def printBoundaryView(self, root):

        if root.left == None and root.right == None:
            return [root.data]

        left_bound = []
        temp = root.left

        if temp:
            while temp:
                left_bound.append(temp.data)

                if temp.left:
                    temp = temp.left
                else:
                    temp = temp.right

        leaf_node = []

        def leaf(temp):
            if temp:
                if not temp.left and not temp.right:
                    leaf_node.append(temp.data)

                leaf(temp.left)
                leaf(temp.right)
        leaf(root)

        # print(leaf_node)

        if len(leaf_node) > 0 and len(left_bound) > 0:
            leaf_node.pop(0)

        right_bound = []
        temp = root.right

        if temp:
            while temp:
                right_bound.append(temp.data)
                if temp.right:
                    temp = temp.right
                else:
                    temp = temp.left

        if len(right_bound) > 0:
            right_bound.pop()

        right_bound.reverse()

        res = [root.data]
        res.extend(left_bound)
        res.extend(leaf_node)
        res.extend(right_bound)

        return res
