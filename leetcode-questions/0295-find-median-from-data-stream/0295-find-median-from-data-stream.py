from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.nums = SortedList([])

    def addNum(self, num: int) -> None:
        self.nums.add(num)

    def findMedian(self) -> float:
        L = len(self.nums)
        if L % 2:
            return self.nums[L // 2]
        else:
            return (self.nums[L // 2] + self.nums[(L // 2) - 1]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()