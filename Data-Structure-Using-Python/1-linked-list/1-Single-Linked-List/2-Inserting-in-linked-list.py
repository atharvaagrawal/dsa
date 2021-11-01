# Inserting Element in a Linked List

# Node Class
class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign Data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # __str__ String Representation of Object
    def __str__(self):
        node = self.head
        output = ""

        while node:
            output += str(node.data) + ","
            node = node.next

        return output

    # Converting List to Linked List
    def list_2_linked_list(self, l):
        if l == []:
            return None

        self.head = Node(l[0])
        n = self.head

        for i in range(1, len(l)):
            new = Node(l[i])
            n.next = new
            n = n.next

    # This function is in LinkedList class
    # Function to insert a new node at the beginning
    def push(self, new_data):

        # 1 & 2: Allocate the Node &
        #        Put in the data
        new_node = Node(new_data)

        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node

    # Appends a new node at the end.
    def append(self, new_data):

        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)

        # 4. If the Linked List is empty, then make the
        #    new node as head
        if self.head is None:
            self.head = new_node
            return

        # 5. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next

        # 6. Change the next of last node
        last.next = new_node

    # new node after the given prev_node.
    def insertAfter(self, position, new_data):
        temp = self.head
        prev_node = ''

        while(temp):
            if temp.data == position:
                prev_node = temp
                break
            temp = temp.next

        # 1. check if the given prev_node exists
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return

        #  2. create new node &
        #      Put in the data
        new_node = Node(new_data)

        # 4. Make next of new Node as next of prev_node
        new_node.next = prev_node.next

        # 5. make next of prev_node as new_node
        prev_node.next = new_node


if __name__ == '__main__':
    list_1 = [1, 3, 5, 7, 9]

    linked_list = LinkedList()
    linked_list.list_2_linked_list(list_1)

    print("Linked List Before Adding:", linked_list)

    print("\n\n")
    # Inserting at the beginning
    newnode = int(input("Enter Node Value:"))
    linked_list.push(newnode)
    print("Linked List After Adding at Start:", linked_list)

    print("\n\n")
    # Inserting at Last
    newnode = int(input("Enter Node Value:"))
    linked_list.append(newnode)
    print("Linked List After Adding at End:", linked_list)

    print("\n\n")
    # Inserting After
    newnode = int(input("Enter Node Value:"))
    position = int(input("Enter Position to insert value after:"))
    linked_list.insertAfter(position, newnode)
    print("Linked List After Adding:", linked_list)
