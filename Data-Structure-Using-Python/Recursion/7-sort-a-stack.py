# Sort a Stack using Recursion

class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def insert(self, temp):
        if len(self.stack) == 0 or self.stack[-1] <= temp:
            self.push(temp)
            return

        last_val = self.pop()

        self.insert(temp)

        self.push(last_val)
        return

    def sort(self):
        if len(self.stack) == 1:
            return

        temp = self.pop()

        self.sort()

        self.insert(temp)

        return


s = Stack()
s.push(1)
s.push(5)
s.push(3)
s.push(2)
print("Before Sort:", s)
s.sort()
print("After Sort:", s)
