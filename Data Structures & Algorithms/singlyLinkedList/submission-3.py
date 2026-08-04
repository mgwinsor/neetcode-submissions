class LinkedList:
    
    def __init__(self):
        self.head = Node(0)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        if not curr:
            return -1

        for _ in range(index):
            curr = curr.next
            if not curr:
                return -1

        return curr.value

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        curr = self.head.next
        self.head.next = new_node
        new_node.next = curr
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        prev = self.head
        curr = self.head.next
        if not curr:
            return False

        for _ in range(index):
            prev = curr
            curr = curr.next
            if not curr:
                return False
        
        prev.next = curr.next
        if curr == self.tail:
            self.tail = prev
        del curr
        return True

    def getValues(self) -> List[int]:
        curr = self.head.next
        values = []
        while curr:
            values.append(curr.value)
            curr = curr.next
        return values

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None