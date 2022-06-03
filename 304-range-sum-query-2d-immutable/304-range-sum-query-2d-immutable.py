class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefixSums = []
        
        for i in range(len(self.matrix)):
            curr = [self.matrix[i][0]]
            for j in range(1, len(self.matrix[i])):
                curr.append(curr[j-1] + self.matrix[i][j])
            self.prefixSums.append(curr)
            
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row1, row2+1):
            total += self.prefixSums[i][col2] - (self.prefixSums[i][col1 - 1] if col1 > 0 else 0)
            
        return total
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)