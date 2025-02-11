class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row_count = len(matrix)
        col_count = len(matrix[0])
        
        transpose = [[0 for _ in range(row_count)] for _ in range(col_count)] 
        
        for i in range(row_count):
            for j in range(col_count):
                transpose[j][i] = matrix[i][j]
        
        return transpose