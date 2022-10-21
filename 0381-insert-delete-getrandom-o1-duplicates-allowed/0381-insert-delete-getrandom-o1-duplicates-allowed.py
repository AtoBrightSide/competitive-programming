class RandomizedCollection:

    def __init__(self):
        self.counter = defaultdict(int)
        self.storeVal = defaultdict(set)
        self.storeInd = []

    def insert(self, val: int) -> bool:
        flag = self.counter[val] == 0
        self.counter[val] += 1
        self.storeVal[val].add(len(self.storeInd))
        self.storeInd.append(val)
        
        return flag

    def remove(self, val: int) -> bool:
        flag = self.counter[val] != 0
        if flag:
            self.counter[val] -= 1
            if self.storeInd[-1] == val:
                self.storeInd.pop()
                self.storeVal[val].remove(len(self.storeInd))
            else:
                temp_index = self.storeVal[val].pop()
                self.storeInd[temp_index], self.storeInd[-1] = self.storeInd[-1], self.storeInd[temp_index]
                self.storeInd.pop()
                
                self.storeVal[self.storeInd[temp_index]].add(temp_index)
                self.storeVal[self.storeInd[temp_index]].remove(len(self.storeInd))
        
        return flag

    def getRandom(self) -> int:
        randomNum = random.randint(0, len(self.storeInd) - 1)
        return self.storeInd[randomNum]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()