# Stack using Deque POP Priority

from collections import deque


class StackWithQueue:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def __str__(self):
        return str(self.q1)

    def pop(self):
        if len(self.q1) + len(self.q2) == 0:
            return "Empty Stack"
        return self.q1.popleft()

    def is_empty(self):
        if len(self.q1) + len(self.q2) == 0:
            return True
        else:
            return False

    def swap(self):
        self.q3 = self.q1
        self.q1 = self.q2
        self.q2 = self.q3

    def push(self, val):
        if len(self.q1) == 0:
            self.q1.append(val)
            return

        self.q2.append(val)

        if self.is_empty():
            return -1
        while len(self.q1) > 0:
            self.q2.append(self.q1.popleft())

        self.swap()


s = StackWithQueue()
s.push(10)
s.push(20)
s.push(30)
print(s)
s.pop()
print("\nAfter Pop:")
print(s)
