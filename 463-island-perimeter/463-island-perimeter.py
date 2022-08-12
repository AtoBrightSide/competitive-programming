class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        DIRS = [[0,1], [1,0], [0,-1], [-1,0]]
        withinBounds = lambda i,j: 0 <= i < len(grid) and 0 <= j < len(grid[0])
        visited = set()
        def traverse(row, col):
            if (row, col) in visited:   return 0
            
            visited.add((row, col))
            count = 0
            for i, j in DIRS:
                new_row, new_col = i + row, j + col
                if withinBounds(new_row, new_col) and grid[new_row][new_col] == 1:
                    count += traverse(new_row, new_col)
                else:
                    count += 1
                    
            return count
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1: 
                    return traverse(row, col)