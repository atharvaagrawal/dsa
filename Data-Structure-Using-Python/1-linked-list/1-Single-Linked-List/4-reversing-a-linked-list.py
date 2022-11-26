# Reversing a Linked List

# Node Class
class ListNode:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign Data
        self.next = None  # Initialize next as null

    # __str__ String Representation of Object
    def __str__(self):
        node = self
        output = ""

        while node:
            output += str(node.data) + ","
            node = node.next

        return output


# Converting List to Linked List
def list_2_linked_list(l):
    if l == []:
        return None

    head = ListNode(l[0])
    n = head

    for i in range(1, len(l)):
        new = ListNode(l[i])
        n.next = new
        n = n.next
    return head


# Reversing a Linked List
def reverse(node):
    prev = None
    curr = node

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


if __name__ == '__main__':
    list_1 = [1, 3, 5, 7, 9]

    node_1 = list_2_linked_list(list_1)

    print("Original:", node_1)

    node_reverse = reverse(node_1)

    print("Reversed:", node_reverse)
