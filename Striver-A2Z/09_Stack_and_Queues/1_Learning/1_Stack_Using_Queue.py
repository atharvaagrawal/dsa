# https://leetcode.com/problems/implement-stack-using-queues/
from queue import Queue


class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        self.q1.put(x)

    def pop(self) -> int:
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

        ele = self.q1.get()

        while not self.q2.empty():
            self.q1.put(self.q2.get())

        return ele

    def top(self) -> int:
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

        element = self.q1.get()
        self.q2.put(element)

        while not self.q2.empty():
            self.q1.put(self.q2.get())

        return element

    def empty(self) -> bool:
        if self.q1.qsize() > 0:
            return False
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
