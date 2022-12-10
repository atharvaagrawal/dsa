# Priority Queue
# A priority queue is a queue in which each element is associated with a priority.
# In a priority queue, an element with high priority is dequeued before an element with low priority.
# If two elements have the same priority, they are served according to their order in the queue.

# Python program to demonstrate working of
# heap queue

import heapq

# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)

# printing created heap
print("The created heap is : ", end="")
print(list(li))

# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li, 4)

# printing modified heap
print("The modified heap after push is : ", end="")
print(list(li))

# using heappop() to pop smallest element
print("The popped and smallest element is : ", end="")
print(heapq.heappop(li))

# printing modified heap
print("The modified heap after pop is : ", end="")
print(list(li))

# using heappushpop() to push and pop items simultaneously
# pops 2
print("The popped item using heappushpop() is : ", end="")
print(heapq.heappushpop(li, 2))

# printing modified heap
print("The modified heap after pushpop is : ", end="")
print(list(li))

# using heapreplace() to push and pop items simultaneously
# pops 3
print("The popped item using heapreplace() is : ", end="")
print(heapq.heapreplace(li, 6))

# printing modified heap
print("The modified heap after replace is : ", end="")
print(list(li))

# Output:
# The created heap is : [1, 3, 9, 7, 5]
# The modified heap after push is : [1, 3, 4, 7, 5, 9]
# The popped and smallest element is : 1
# The modified heap after pop is : [3, 5, 4, 7, 9]
# The popped item using heappushpop() is : 2
# The modified heap after pushpop is : [3, 5, 4, 7, 9]
# The popped item using heapreplace() is : 3
# The modified heap after replace is : [4, 5, 6, 7, 9]

