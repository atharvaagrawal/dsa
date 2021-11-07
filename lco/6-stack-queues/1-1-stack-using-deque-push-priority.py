from collections import deque


class StackWithQ:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def __str__(self):
        return str(self.q1)

    def push(self, val):
        self.q1.append(val)

    def is_empty(self):
        if len(self.q1) + len(self.q2) == 0:
            return True
        else:
            return False

    def swap(self):
        self.q3 = self.q1
        self.q1 = self.q2
        self.q2 = self.q3

    def pop(self):
        if self.is_empty():
            return -1
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        value_to_be_returned = self.q1.popleft()
        self.swap()
        return value_to_be_returned


s = StackWithQ()
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
