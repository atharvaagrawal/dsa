# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

""" 
Serialization is the process of converting a data structure or object into a sequence of bits 
so that it can be stored in a file or memory buffer, or transmitted across a network connection
link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how 
your serialization/deserialization algorithm should work. You just need to ensure that a binary 
tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do 
not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return ''

        data = []

        # Using level order traversal
        q = [root]

        while q:
            n = len(q)

            for i in range(n):
                node = q.pop(0)

                if not node:
                    data.append('#,')
                else:
                    data.append(str(node.val)+',')

                if node:
                    q.append(node.left)
                    q.append(node.right)

        return ''.join(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        l = data.split(',')
        l.pop()

        if len(l) == 0:
            return None

        root = TreeNode(l[0])

        q = [root]
        i = 1

        while q and i < len(l):
            node = q.pop(0)

            if l[i] != '#':
                left = TreeNode(int(l[i]))
                node.left = left
                q.append(node.left)

            i += 1

            if l[i] != '#':
                right = TreeNode(int(l[i]))
                node.right = right
                q.append(right)

            i += 1

        # print(root)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
