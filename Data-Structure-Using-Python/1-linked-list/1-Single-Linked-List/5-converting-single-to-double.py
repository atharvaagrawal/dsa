# Creating a Double Linked List
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return "Linked List is Empty"

        temp = self.head

        output = ""
        while temp:
            output += str(temp.val) + " "
            temp = temp.next
        return output

    # Inserting a Node at beginning
    def insert_at_start(self, new_val):
        new_node = Node(new_val)

        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    # Inserting at a Position
    def insert_at_position(self, prev_node, val):
        new_node = Node(val)

        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next = new_node
        new_node.next.prev = new_node

    # Converting List to Linked List
    def list_2_linked_listI(self, l):
        j = 0
        if self.head is None:
            self.head = Node(l[0])
            fact = 0
            j = 1
        else:
            temp = self.head
            while temp.next:
                print('h')
                temp = temp.next
            fact = 1

        if fact == 0:
            n = self.head
        else:
            n = temp

        for i in range(j, len(l)):
            new_node = Node(l[i])
            n.next = new_node
            new_node.prev = n
            n = n.next
        return


dll = DoublyLinkedList()

dll.insert_at_start(10)

dll.insert_at_start(12)
print(dll)
dll.list_2_linked_listI([20, 30, 40, 50])
#dll.insert_at_position(dll.head.next.next, 25)

print(dll)
