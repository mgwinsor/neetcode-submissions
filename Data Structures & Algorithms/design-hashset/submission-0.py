class MyHashSet:

    def __init__(self):
        self.keys = [0] * 1007

    def add(self, key: int) -> None:
        hash = key % 1007
        if self.keys[hash] == 0:
            self.keys[hash] = key

    def remove(self, key: int) -> None:
        hash = key % 1007        
        self.keys[hash] = 0

    def contains(self, key: int) -> bool:
        hash = key % 1007
        return True if self.keys[hash] != 0 else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)