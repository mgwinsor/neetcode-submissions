class MyQueue:

    def __init__(self):
        self.q = []
        self.length = 0

    def push(self, x: int) -> None:
        self.q.append(x)
        self.length += 1

    def pop(self) -> int:
        val = self.q[0]
        self.q = self.q[1:]
        self.length -= 1
        return val

    def peek(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return self.length == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()