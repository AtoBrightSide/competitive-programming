class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix) - 1
        for row in matrix:
            if self.mybin(row, target):
                return True
            
        return False
    def mybin(self, row, target):
        l,r = 0, len(row)-1
        while l<=r:
            md = l + (r-l)//2
            if row[md]>target:
                r = md-1
            elif row[md]<target:
                l = md+1
            else:
                return True
        return False
