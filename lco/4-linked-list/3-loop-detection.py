
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def list_2_linked_list(self, l):
        self.head = Node(l[0])

        temp = self.head

        for i in range(1, len(l)):
            new_node = Node(l[i])
            temp.next = new_node
            temp = temp.next

        # Making Loop
        new_node.next = self.head.next.next


# Checking using Flyod Algorithm
def has_cycle(head):
    if not head:
        return False

    if head.next == None:
        return False

    if head.next.next == None:
        return False

    fast = head
    slow = head

    while fast != None and slow != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            return True

    return False

# Checking Using Diary


def has_cycle_with_diary(head):
    # take care of No Head, 1 value, 2 value

    diary = {}

    while head:
        if head in diary:
            return True
        else:
            diary[head] = True
        head = head.next

    return False


ll = LinkedList()
ll.list_2_linked_list([10, 20, 30, 40, 50, 60, 70, 80])

print(has_cycle(ll.head))
print(has_cycle_with_diary(ll.head))
