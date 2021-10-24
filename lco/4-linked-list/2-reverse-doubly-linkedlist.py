# Reverse A Doubly Linked List

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        # Checking LinkedList is Empty or Not
        if self.head is None:
            return "LinkedList is Empty"

        temp = self.head
        output = ""

        while temp:
            output += str(temp.val) + " "
            temp = temp.next
        return output

    def list_2_linked_list(self, l):
        self.head = Node(l[0])

        prev_node = self.head

        for i in range(1, len(l)):
            new_node = Node(l[i])
            prev_node.next = new_node
            new_node.prev = prev_node
            prev_node = new_node

    # Reverse a Linked List
    def reverse(self):
        temp = self.head

        while(temp.next):
            swap = temp.prev
            temp.prev = temp.next
            temp.next = swap
            temp = temp.prev

        temp.next = temp.prev
        temp.prev = None

        self.head = temp

    # Printing Reverse a Linked List Using Recurrsion
    def reverse_recurr(self, travel):
        if travel.next is None:
            print(travel.val, end=" ")
            return
        self.reverse(travel.next)
        print(travel.val, end=" ")


dll = DoublyLinkedList()

dll.list_2_linked_list([10, 20, 30, 40])
print("Original List:", dll)

print("Reverse Linked List:", end=" ")
dll.reverse()
print(dll)
