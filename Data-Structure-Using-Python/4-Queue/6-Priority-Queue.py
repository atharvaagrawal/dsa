import queue

q = queue.PriorityQueue()

q.put(10)
q.put(60)
q.put(20)
q.put(40)
q.put(40)

while not q.empty():
    print(q.get())

# Output:
# 10
# 20
# 40
# 40
# 60
