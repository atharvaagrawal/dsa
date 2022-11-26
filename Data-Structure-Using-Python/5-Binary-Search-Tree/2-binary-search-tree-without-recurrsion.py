# Python program to demonstrate
# insert operation in binary search tree

# A utility class that represents
# an individual node in a BST


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


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

    def iterativeSearch(self, root, key):
        # Traverse until root reaches
        # to dead end
        while root != None:

            # pass right subtree as new tree
            if key > root.data:
                root = root.right

            # pass left subtree as new tree
            elif key < root.data:
                root = root.left
            else:
                return True  # if the key is found return 1
        return False

    # Iterative function for inorder tree traversal

    def inorder(self, root):

        # Set current to root of binary tree
        current = root
        stack = []  # initialize stack
        done = 0

        while True:

            # Reach the left most Node of the current Node
            if current is not None:

                # Place pointer to a tree node on the stack
                # before traversing the node's left subtree
                stack.append(current)

                current = current.left

            # BackTrack from the empty subtree and visit the Node
            # at the top of the stack; however, if the stack is
            # empty you are done
            elif(stack):
                current = stack.pop()
                print(current.data, end=" ")  # Python 3 printing

                # We have visited the node and its left
                # subtree. Now, it's right subtree's turn
                current = current.right

            else:
                break

        print()

    # Helper function that allocates a new node with the
    # given data and NULL left and right pointers.
    def postorder(self, head):
        temp = head
        visited = set()
        while (temp and temp not in visited):

            # Visited left subtree
            if (temp.left and temp.left not in visited):
                temp = temp.left

            # Visited right subtree
            elif (temp.right and temp.right not in visited):
                temp = temp.right

            # Print node
            else:
                print(temp.data, end=" ")
                visited.add(temp)
                temp = head

    # Function to traverse tree without recursion
    def preorder(self, root):
        # Base CAse
        if root is None:
            return

        # create an empty stack and push root to it
        nodeStack = []
        nodeStack.append(root)

        # Pop all items one by one. Do following for every popped item
        # a) print it
        # b) push its right child
        # c) push its left child
        # Note that right child is pushed first so that left
        # is processed first */
        while(len(nodeStack) > 0):

            # Pop the top item from stack and print it
            node = nodeStack.pop()
            print(node.data, end=" ")

            # Push right and left children of the popped node
            # to stack
            if node.right is not None:
                nodeStack.append(node.right)
            if node.left is not None:
                nodeStack.append(node.left)


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


print("\n\nSearch:", bst.iterativeSearch(bst.root, 450))
