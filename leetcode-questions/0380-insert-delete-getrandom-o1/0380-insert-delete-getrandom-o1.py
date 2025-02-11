class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.list = []

    def insert(self, val: int) -> bool:
        not_present = val not in self.map
        if not_present:
            self.map[val] = len(self.list)
            self.list.append(val)
        
        return not_present

    def remove(self, val: int) -> bool:
        present = val in self.map
        if present:
            idx = self.map[val]
            self.list[idx], self.list[-1] = self.list[-1], self.list[idx]
            self.map[self.list[idx]] = idx
            self.list.pop()
            del self.map[val]
            
        return present

    def getRandom(self) -> int:
        idx = int(random.random() * len(self.list))
        return self.list[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()