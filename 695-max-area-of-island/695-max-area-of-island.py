class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        isValid = lambda i,j: 0 <= i < len(grid) and 0 <= j < len(grid[0])
        
        DIRS = [[0,1],[1,0],[0,-1],[-1,0]] 
        visited = set()
        
        def dp(i, j):
            count = 0
            visited.add((i, j))
            for d in DIRS:
                x, y = d[0] + i, d[1] + j
                if isValid(x, y) and (x, y) not in visited and grid[x][y] == 1:
                    count += 1 + dp(x, y)
                    
            return count
        
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, 1 + dp(i, j))
            
            
        return max_area