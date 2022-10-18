class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        self.matrix = [[0] * n for _ in range(n)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
        new_row = cur_row = 0
        new_col = cur_col = 0
        cur_direction = 0
        val = 1
        cells = n * n
        
        while val <= cells:
            self.matrix[cur_row][cur_col] = val

            new_row = cur_row + directions[cur_direction % 4][0]
            new_col = cur_col + directions[cur_direction % 4][1]
            
            if not self.isValid(new_row, new_col, n):
                cur_direction += 1
            
            cur_row += directions[cur_direction % 4][0]
            cur_col += directions[cur_direction % 4][1]
            val += 1
        
        return self.matrix
    
    def isValid(self, cur_row, cur_col, n):
        return 0 <= cur_row < n and 0 <= cur_col < n and self.matrix[cur_row][cur_col] == 0