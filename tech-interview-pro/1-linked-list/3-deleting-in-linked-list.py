# Deleting Elements in Linked List

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList Class
class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        node = self.head
        output = ""

        while node:
            output += str(node.data) + ","
            node = node.next

        return output

    def list_2_linked_list(self, l):
        if l == []:
            return None

        self.head = Node(l[0])
        n = self.head

        for i in range(1, len(l)):
            new = Node(l[i])
            n.next = new
            n = n.next

    # Given a reference to the head of a list and a key,
    # delete the first occurrence of key in linked list
    def deleteNode(self, key):
        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        prev = ''
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if(temp == None):
            print("Node Not Present")
            return

        # Unlink the node from linked list
        prev.next = temp.next
        temp = None

    # Delete All Node
    def deleteAllNodes(self):
        current = self.head
        while current:
            prev = current.next  # move next node

            # delete the current node
            del current.data

            # set current equals prev node
            current = prev

        # In python garbage collection happens
        # therefore, only
        self.head = None
        # would also delete the link list


l = [1, 2, 3, 4, 5]
ll = LinkedList()

ll.list_2_linked_list(l)
print("Linked List before Deletion:", ll)

# Deleting a Node
key = int(input("Enter Node to be Deleted:"))
ll.deleteNode(key)
print("Linked List After Deletion:", ll)

# Delete All Node
ll.deleteAllNodes()
print("After Deleting All Node", ll)
