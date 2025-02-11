class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        
        '''
        numROws = 5
        row = 5
        cur_row = [1,4,6,4,1]
        col = 4
        pascal = [[1],[1,1],[1,2,1], [1,3,3,1],[1,4,6,4,1]]
        '''
        
        for row in range(1, numRows+1):
            current_row = [1] * row
            for col in range(row):
                if col != 0 and col != row - 1:
                    current_row[col] = (pascal[-1][col-1] + pascal[-1][col])
            
            pascal.append(current_row)
        
        return pascal
                    