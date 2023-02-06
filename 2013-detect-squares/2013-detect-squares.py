class DetectSquares:
    def __init__(self):
        self.square = Counter()
        self.x = defaultdict(Counter)   # x -> all y coordinates with freqs

    def add(self, point):
        x, y = point
        self.square[x, y] += 1
        self.x[x][y] += 1

    def count(self, point):
        x, y = point
        ans = 0
        for y2 in self.x[x]:
            if y == y2: continue
            ans += self.square[x, y2] * self.square[x + y2 - y, y] * self.square[x + y2 - y, y2]
            ans += self.square[x, y2] * self.square[x + y - y2, y] * self.square[x + y - y2, y2]
        return ans