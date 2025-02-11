class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:        
        ones = 0
        for i in range(len(grid)):  
            for j in range(len(grid[i])):   ones += 1 if grid[i][j] == 1 else 0
        
        isValid = lambda i,j: 0 <= i < len(grid) and 0 <= j < len(grid[0])
        isEdge = lambda i,j: i == 0 or i == len(grid) -1 or j == 0 or j == len(grid[i]) - 1
        
        DIRS = [[0,1],[1,0],[0,-1],[-1,0]]
        counted = set()
        def dfs(i, j):
            if (i, j) in counted:   return
            
            counted.add((i, j))
            for d in DIRS:
                x, y = d[0] + i, d[1] + j
                if isValid(x, y) and grid[x][y] == 1:   dfs(x, y)
            
            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if isEdge(i, j) and grid[i][j] == 1:    dfs(i, j)
                    
        return ones - len(counted)