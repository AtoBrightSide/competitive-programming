class MyHashSet:

    def __init__(self):
        self.myset = []

    def add(self, key: int) -> None:
        if key in self.myset:
            return
        self.myset.append(key)
            

    def remove(self, key: int) -> None:
        for i in range(len(self.myset)):
            if self.myset[i] == key:
                self.myset[i] = self.myset[-1]
                self.myset.pop()
                return

    def contains(self, key: int) -> bool:
        return key in self.myset


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)