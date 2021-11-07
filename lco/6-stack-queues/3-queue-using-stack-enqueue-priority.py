# Queue Using Stack when enqueue is having priority

class QueueWithS:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def is_empty(self):
        if len(self.s2) + len(self.s1) == 0:
            return True
        else:
            return False

    def __str__(self):
        output = ""

        if self.is_empty():
            return "Empty"

        output = str(self.s1) + str(self.s2)
        return output

    def enque(self, val):
        self.s1.append(val)

    def deque(self):
        if self.is_empty():
            return "Empty"

        if len(self.s2) == 0:
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())
            print(self.s2)

        return self.s2.pop()


q = QueueWithS()

q.enque(10)
q.enque(20)
q.enque(30)
q.enque(40)

print(q)

print("Deque:", q.deque())
print(q)
q.enque(50)
print(q)
print("Deque 2:", q.deque())
print(q)
