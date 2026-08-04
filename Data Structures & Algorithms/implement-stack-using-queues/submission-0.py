class MyStack:

    def __init__(self):
        self.stack = deque()
        self.length = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.length += 1

        if self.length > 1:
            for i in range(self.length - 1):
                val = self.stack.popleft()
                self.stack.append(val)

    def pop(self) -> int:
        self.length -= 1
        return self.stack.popleft()

    def top(self) -> int:
        top_val = self.pop()
        self.push(top_val)
        return top_val

    def empty(self) -> bool:
        if self.length > 0:
            return False
        return True