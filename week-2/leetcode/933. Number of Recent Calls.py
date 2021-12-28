class RecentCounter:

    def __init__(self):
        self.myqueue=deque()
    def ping(self, t: int) -> int:
        self.myqueue.append(t)
        while self.myqueue[0]<t-3000:
            self.myqueue.popleft()
        return len(self.myqueue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
