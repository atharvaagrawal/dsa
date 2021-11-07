# Implement Stack Using Queues

class Queue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return str(self.queue)

    def enque(self, val):
        self.queue.append(val)

    def deque(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)


# Implementing Stacks
class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def __str__(self):
        return str(self.q1)

    def push(self, val):
        self.q1.enque(val)

    def pop(self):
        if self.q1.size() == 0 and self.q2.size() == 0:
            print("Empty Stack")
            return

        if self.q1.size() > 0:
            for i in range(0, self.q1.size()-1):
                self.q2.enque(self.q1.deque())

        pop_res = self.q1.deque()

        # Swapping References
        ref = self.q1
        self.q1 = self.q2
        self.q2 = ref

        return pop_res

    def is_empty(self):
        if self.q1.size() + self.q2.size() == 0:
            return True
        else:
            return False


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)

print(s)
print(s.pop())
print(s)
s.push(50)
print(s)
print(s.is_empty())
