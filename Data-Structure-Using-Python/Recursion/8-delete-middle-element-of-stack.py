# Delate middle element of a Stack using Recursion

class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def delete(self, mid):
        if len(self.stack)-1 == mid:
            self.pop()
            return

        val = self.pop()

        self.delete(mid)

        self.push(val)

    def delete_middle(self):

        self.delete(len(self.stack)//2)

        return


s = Stack()
s.push(1)
s.push(5)
s.push(3)
s.push(2)
s.push(4)
print("Before Delete:", s)
s.delete_middle()
print("After Delete:", s)
