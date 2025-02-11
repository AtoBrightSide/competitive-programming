class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        # count all required variables to calculate the diff
        onesRow = []
        zerosRow = []
        for i in range(len(grid)):
            ones = zeros = 0
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    ones += 1
                if grid[i][j] == 0:
                    zeros += 1
            onesRow.append(ones)
            zerosRow.append(zeros)
        
        onesCol = []
        zerosCol = []
        for j in range(len(grid[0])):
            ones = zeros = 0
            for i in range(len(grid)):
                if grid[i][j] == 1:     ones += 1
                else:                   zeros += 1
            
            onesCol.append(ones)
            zerosCol.append(zeros)
        
        diff = []
        for i in range(len(grid)):
            curr_row = []
            for j in range(len(grid[0])):
                curr_diff = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]
                curr_row.append(curr_diff)
            diff.append(curr_row)
        
        return diff