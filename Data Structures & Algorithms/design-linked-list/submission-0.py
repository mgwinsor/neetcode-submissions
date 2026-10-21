class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def _getPrev(self, index) -> Node:
        if index <= self.size // 2:
            cur = self.head
            for _ in range(index):
                cur = cur.next
        else:
            cur = self.tail
            for _ in range(self.size - index + 1):
                cur = cur.prev
        return cur

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        return self._getPrev(index).next.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        prev = self._getPrev(index)
        next = prev.next
        new = Node(val)

        prev.next = new
        new.next = next

        next.prev = new
        new.prev = prev

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        prev = self._getPrev(index)
        old = prev.next
        next = old.next

        prev.next = next
        next.prev = prev

        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)