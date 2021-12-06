# Reverse a Stack using Recursion

class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def insert(self, val):
        if len(self.stack) == 0:
            self.push(val)
            return

        temp = self.pop()

        self.insert(val)

        self.push(temp)
        return

    def reverse(self):
        if len(self.stack) == 1:
            return

        temp = self.pop()

        self.reverse()

        self.insert(temp)
        return


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print("Before Reverse:", s)
s.reverse()
print("After Reverse:", s)
