# Merging 2 Sorted Linked List

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
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

        temp = self.head

        for i in range(1, len(l)):
            new_node = Node(l[i])
            temp.next = new_node
            temp = temp.next


def merge(head_1, head_2, head_3):
    if head_1.val < head_2.val:
        head_3 = Node(head_1.val)
        head_1 = head_1.next
    else:
        head_3 = Node(head_2.val)
        head_2 = head_2.next

    temp = head_3

    while head_1 is not None and head_2 is not None:
        if head_1.val < head_2.val:
            temp.next = Node(head_1.val)
            head_1 = head_1.next
        else:
            temp.next = Node(head_2.val)
            head_2 = head_2.next
        temp = temp.next

    loop = 0
    if head_1 is not None:
        loop = head_1
    else:
        loop = head_2

    while loop:
        temp.next = Node(loop.val)
        loop = loop.next
        temp = temp.next
    return head_3


def merge_sorted_linkedlist(head1, head2):
    # corner cases
    if head1 is None:
        return head2  # list1 is not there

    if head2 is None:
        return head1  # ask

    ll3_head = None

    if head1.val <= head2.val:
        ll3_head = head1
        head1 = head1.next
    else:
        ll3_head = head2
        head2 = head2.next

    ll3_tail = ll3_head

    while head1 and head2:
        temp = None

        if head1.val <= head2.val:
            temp = head1
            head1 = head1.next
        else:
            temp = head2
            head2 = head2.next

        ll3_tail.next = temp
        ll3_tail = temp

    if head1:
        ll3_tail.next = head1
    elif head2:
        ll3_tail.next = head2
    return ll3_head


list_1 = LinkedList()
list_1.list_2_linked_list([8, 9, 12, 15, 20, 25, 30])

list_2 = LinkedList()
list_2.list_2_linked_list([7, 10, 11, 13])


list_3 = LinkedList()
list_3.head = merge(list_1.head, list_2.head, list_3.head)

print("List1:", list_1)
print("List2:", list_2)
print("List3:", list_3)
