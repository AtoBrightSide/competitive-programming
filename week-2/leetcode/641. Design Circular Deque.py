class MyCircularDeque:
    def __init__(self, k: int):
        self.mydeq = []
        self.length = k

    def insertFront(self, value: int) -> bool:
        if len(self.mydeq) >= self.length:
            return False
        else:
            self.mydeq.insert(0, value)
            return True

    def insertLast(self, value: int) -> bool:
        if len(self.mydeq) >= self.length:
            return False
        else:
            self.mydeq.append(value)
            return True

    def deleteFront(self) -> bool:
        if len(self.mydeq) <= 0:
            return False
        else:
            self.mydeq.remove(self.mydeq[0])
            return True

    def deleteLast(self) -> bool:
        if len(self.mydeq) <= 0:
            return False
        else:
            self.mydeq.pop()
            return True

    def getFront(self) -> int:
        if len(self.mydeq) != 0:
            return self.mydeq[0]
        return -1

    def getRear(self) -> int:
        if len(self.mydeq) != 0:
            return self.mydeq[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.mydeq) == 0

    def isFull(self) -> bool:
        return len(self.mydeq) == self.length


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
