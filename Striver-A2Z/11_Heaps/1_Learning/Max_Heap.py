from queue import PriorityQueue


class MaxHeapElement:
    def __init__(self, priority, item):
        self.priority = priority
        self.item = item

    def __lt__(self, other):
        return self.priority > other.priority


q = PriorityQueue()

# insert into queue
q.put(MaxHeapElement(2, 'g'))
q.put(MaxHeapElement(3, 'e'))
q.put(MaxHeapElement(4, 'k'))
q.put(MaxHeapElement(5, 's'))
q.put(MaxHeapElement(1, 'e'))

# iterate over all elements in max heap
while not q.empty():
    element = q.get().item
    print(element)

"""
Another Way
"""

q = PriorityQueue()

# insert into queue with negated priorities for max heap
q.put((-2, 'g'))
q.put((-3, 'e'))
q.put((-4, 'k'))
q.put((-5, 's'))
q.put((-1, 'e'))

# iterate over all elements in max heap
while not q.empty():
    priority, element = q.get()
    print(element)
