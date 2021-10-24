# Creating a Linked List

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
            output = output + "["+str(node.data) + \
                " " + str(id(node.next))+"] "
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
        #print(n, id(n))
    return head


if __name__ == '__main__':
    list_1 = [1, 3, 5, 7, 9]
    list_2 = [2, 4, 6, 8, 10]

    node_1 = list_2_linked_list(list_1)
    node_2 = list_2_linked_list(list_2)

    print(node_1)
    print()
    print(node_2)
