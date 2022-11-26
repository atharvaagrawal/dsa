# Implement Queue Using Stack when dequeue is having priority

class QUsingStack:
    def __init__(self):
        self.res = []
        self.s2 = []

    def __str__(self):
        return str(self.res)

    def is_empty(self):
        if len(self.res) + len(self.s2) == 0:
            return True
        else:
            return False

    def enqueue(self, val):
        if len(self.res) == 0:
            self.res.append(val)
            return

        while len(self.res) > 0:
            self.s2.append(self.res.pop())

        self.res.append(val)

        while len(self.s2) > 0:
            self.res.append(self.s2.pop())

    def dequeue(self):
        if self.is_empty():
            return "Empty"

        return self.res.pop()


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
