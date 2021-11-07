# Implement Queue Using Stack when dequeue is having priority

class QUsingStack:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def __str__(self):
        return str(self.s1)

    def is_empty(self):
        if len(self.s1) + len(self.s2) == 0:
            return True
        else:
            return False

    def enqueue(self, val):
        if len(self.s1) == 0:
            self.s1.append(val)
            return

        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())

        self.s1.append(val)

        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())

    def dequeue(self):
        if self.is_empty():
            return "Empty"

        return self.s1.pop()


q = QUsingStack()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print(q)

print("Deque:", q.dequeue())
print(q)
q.enqueue(50)
print(q)
print("Deque 2:", q.dequeue())
print(q)
