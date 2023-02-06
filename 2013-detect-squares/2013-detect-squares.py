class DetectSquares:

    def __init__(self):
        self.x = defaultdict(set)
        self.square = defaultdict(int)
        
    def add(self, point: List[int]) -> None:
        x, y = point
        self.x[x].add(y)
        self.square[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        num_of_squares = 0
        x1, y1 = point
        for y2 in self.x[x1]:
            L = abs(y2 - y1)
            if y1 != y2:
                side1 = (x1 + L, y1)
                side3 = (x1 + L, y2)

                _side1 = (x1 - L, y1)
                _side3 = (x1 - L, y2)
                
                num_of_squares += self.square[side1] * self.square[(x1, y2)] * self.square[side3]
                num_of_squares += self.square[_side1] * self.square[(x1, y2)] * self.square[_side3]
        
        return num_of_squares