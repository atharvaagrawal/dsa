# DFS = Depth First Search

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        # print(value)

        if self.root == None:
            self.root = Node(value);
            return
        elif self.root.left == None:
            self.root.left = Node(value)
            # print(value)
            return
        elif self.root.right == None:
            self.root.right = Node(value)
            # print(value,end=" ")
            return

        templ = self.root
        tempr = self.root
        # print(value)
        countl = 0
        countr = 0

        while(templ.left != None and templ.right != None):
            templ = templ.left
            countl +=1

        # Balanced Tree
        while(tempr.left != None and tempr.right != None):
            tempr = tempr.right
            countr +=1
        
        if countr < countl:
            if tempr.left == None:
                tempr.left = Node(value)
            else:
                tempr.right = Node(value)
        else:
            if templ.left == None:
                templ.left = Node(value)
            else:
                templ.right = Node(value)
        

    def inorder(self,root):
        if root == None:
            return
        
        self.inorder(root.left) 
        print(root.data,end=" ")
        self.inorder(root.right)

    def postorder(self,root):
        if root == None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data,end=" ")

    def preorder(self,root):
        if root == None:
            return
        print(root.data,end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

bt = BSTree()

bt.insert(1)
bt.insert(2)
bt.insert(3)
    
bt.insert(4)
bt.insert(5)
bt.insert(6)
bt.insert(7)

print("\n\n Inorder Traversal: ")
bt.inorder(bt.root) 

print("\n\n Pre-order Traversal: ")
bt.preorder(bt.root)

print("\n\n Post-order Traversal: ")
bt.postorder(bt.root)


# print(bt.root.left.data)

