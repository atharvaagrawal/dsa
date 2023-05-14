from queue import PriorityQueue

q = PriorityQueue()

# insert into queue
q.put((2, 'g'))
q.put((3, 'e'))
q.put((4, 'k'))
q.put((5, 's'))
q.put((1, 'e'))

# iterate over all elements in min heap
while not q.empty():
    priority, element = q.get()
    print(priority, element)
