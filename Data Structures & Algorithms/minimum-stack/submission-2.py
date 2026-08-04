class MinStack:

    def __init__(self):
        self.stack = []
        self.min_order = []

    def push(self, val: int) -> None:
        if len(self.min_order) == 0 or self.min_order[-1] >= val:
            self.min_order.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min_order[-1]:
            self.min_order.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        return self.min_order[-1]
