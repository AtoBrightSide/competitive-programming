class DetectSquares:

    def __init__(self):
        self.x = defaultdict(set)
        self.square = defaultdict(int)
        
    def add(self, point: List[int]) -> None:
        x, y = point
        self.x[x].add(y)
        self.square[(x, y)] += 1

    def check(self, x1, y1, x2, y2, L):
        side1 = (x1 + L, y1)
        side3 = (x2 + L, y2)
        
        _side1 = (x1 - L, y1)
        _side3 = (x2 - L, y2)
        
        ans = 0
        ans += self.square[side1] * self.square[(x2, y2)] * self.square[side3]
        ans += self.square[_side1] * self.square[(x2, y2)] * self.square[_side3]
        
        return ans
    
    def count(self, point: List[int]) -> int:
        num_of_squares = 0
        x, y = point
        for y_pt in self.x[x]:
            if y_pt != y:
                num_of_squares += self.check(x, y, x, y_pt, abs(y - y_pt))
        
        return num_of_squares