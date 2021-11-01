# Creating Circular Linked List

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return "Empty"
        output = ""
        temp = self.head

        while temp.next != self.head:
            output += str(temp.val) + " "
            temp = temp.next
        output += str(temp.val) + " "

        return output

    def insert_at_start(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return

        temp = self.head
        temp2 = self.head
        self.head = new_node
        new_node.next = temp

        while temp.next != temp2:
            temp = temp.next

        temp.next = self.head

    def insert_at_end(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return

        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    def delete(self, val):
        temp = self.head
        prev = None
        check = 0

        while temp.next != self.head:
            if temp.val == val:
                check = 1
                break
            prev = temp
            temp = temp.next

        if temp.val == val:
            check = 1

        if check == 0:
            print("Element not Present")
            return

        if prev is None:
            temp2 = temp.next
            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            temp.next = temp2
            self.head = temp2
            return

        prev.next = temp.next
        temp.next = None


cll = CircularLinkedList()

cll.insert_at_end(40)
cll.insert_at_end(50)
cll.insert_at_end(60)

cll.insert_at_start(30)
print(cll)
cll.delete(30)
print(cll)
cll.insert_at_end(70)
cll.insert_at_end(80)
print(cll)
