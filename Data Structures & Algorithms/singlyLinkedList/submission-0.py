class LinkedList:
    
    def __init__(self):
        self.dummy = Node(0)
    
    def get(self, index: int) -> int:
        curr = self.dummy.next
        if not curr:
            return -1

        for _ in range(index):
            curr = curr.next
            if not curr:
                return -1

        return curr.value

    def insertHead(self, val: int) -> None:
        old_head = self.dummy.next
        self.dummy.next = Node(val)
        self.dummy.next.next = old_head

    def insertTail(self, val: int) -> None:
        curr = self.dummy.next
        if not curr:
            self.dummy.next = Node(val)
            return

        while curr:
            if not curr.next:
                curr.next = Node(val)
                return
            curr = curr.next

    def remove(self, index: int) -> bool:
        prev = self.dummy
        curr = self.dummy.next
        if not curr:
            return False

        for _ in range(index):
            prev = curr
            curr = curr.next
            if not curr:
                return False
        
        prev.next = curr.next
        del curr
        return True

    def getValues(self) -> List[int]:
        curr = self.dummy.next
        values = []
        while curr:
            values.append(curr.value)
            curr = curr.next
        return values

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None