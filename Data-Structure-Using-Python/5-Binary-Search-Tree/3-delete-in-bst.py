
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

    def delete(self, key):
        curr = self.root
        prev = None

        # First check if the key is
        # actually present in the BST.
        # the variable prev points to the
        # parent of the key to be deleted
        while(curr != None and curr.data != key):
            prev = curr
            if curr.data < key:
                curr = curr.right
            else:
                curr = curr.left

        if curr == None:
            print("Key % d not found in the provided BST." % key)
            return

        # Check if the node to be
        # deleted has atmost one child
        if curr.left == None or curr.right == None:

            # newCurr will replace
            # the node to be deleted.
            newCurr = None

            # if the left child does not exist.
            if curr.left == None:
                newCurr = curr.right
            else:
                newCurr = curr.left

            # check if the node to
            # be deleted is the root.
            if prev == None:
                return newCurr

            # Check if the node to be
            # deleted is prev's left or
            # right child and then
            # replace this with newCurr
            if curr == prev.left:
                prev.left = newCurr
            else:
                prev.right = newCurr

            curr = None

        # node to be deleted
        # has two children.
        else:
            p = None
            temp = None

            # Compute the inorder
            # successor of curr.
            temp = curr.right
            while(temp.left != None):
                p = temp
                temp = temp.left

            # check if the parent of the
            # inorder successor is the root or not.
            # if it isn't, then make the left
            # child of its parent equal to the
            # inorder successor's right child.
            if p != None:
                p.left = temp.right

            else:

                # if the inorder successor was
                # the root, then make the right child
                # of the node to be deleted equal
                # to the right child of the inorder
                # successor.
                curr.right = temp.right

            curr.data = temp.data
            temp = None

        return

    # Left-->Parent-->Right

    def inorder(self, root):
        if root:
            # First recur on left child
            self.inorder(root.left)

            # then print the data of node
            print(root.data, end=" ")

            # now recur on right child
            self.inorder(root.right)


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
bst.insert(10)
bst.insert(35)
bst.insert(44)

print(" InOrder:", end=" ")
bst.inorder(bst.root)

print("\n\n")

bst.delete(30)
print(" InOrder:", end=" ")
bst.inorder(bst.root)
