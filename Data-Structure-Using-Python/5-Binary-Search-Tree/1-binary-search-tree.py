# Implementing Binary Search Tree

# Left Side: Smaller Values
# Right Side: Larger Values

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BSTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        # First Node
        if(self.root == None):
            self.root = new_node
            return

        # Place node at its position
        temp = self.root
        parent = None
        while(temp):
            parent = temp

            # duplicate
            if temp.data == new_node.data:
                break

            # Right Node
            if temp.data < new_node.data:
                temp = temp.right
            # Left Node
            elif temp.data > new_node.data:
                temp = temp.left

        if parent.data < new_node.data:
            parent.right = new_node
        elif parent.data > new_node.data:
            parent.left = new_node

    # A utility function to search a given key in BST

    def search(self, root, key):
        # Base Cases: root is null or key is present at root
        if root is None or root.data == key:
            return root

        # Key is greater than root's key
        if root.data < key:
            return self.search(root.right, key)

        # Key is smaller than root's key
        return self.search(root.left, key)

    # A function to do inorder tree traversal
    # Left-->Parent-->Right
    def inorder(self, root):
        if root:
            # First recur on left child
            self.inorder(root.left)

            # then print the data of node
            print(root.data, end=" ")

            # now recur on right child
            self.inorder(root.right)

    # A function to do postorder tree traversal
    # Left-->Right-->Parent
    def postorder(self, root):
        if root:
            # First recur on left child
            self.postorder(root.left)

            # the recur on right child
            self.postorder(root.right)

            # now print the data of node
            print(root.data, end=" ")

    # A function to do preorder tree traversal
    # Parent --> Left --> Right
    def preorder(self, root):
        if root:
            # First print the data of node
            print(root.data, end=" ")

            # Then recur on left child
            self.preorder(root.left)

            # Finally recur on right child
            self.preorder(root.right)


bst = BSTree()

bst.insert(50)
bst.insert(30)
bst.insert(60)
bst.insert(20)
bst.insert(40)
bst.insert(55)
bst.insert(57)
bst.insert(70)
bst.insert(50)


print(" InOrder:", end=" ")
bst.inorder(bst.root)

print("\n\n Pre-Order:", end=" ")
bst.preorder(bst.root)

print("\n\n Post-Order:", end=" ")
bst.postorder(bst.root)

res = bst.search(bst.root, 40)

if res:
    print("\n\nSearch: ", res.data)
else:
    print("\n\nValue is Not Present")
