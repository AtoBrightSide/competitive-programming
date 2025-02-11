class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # formula for making each cell unique: (no of cols * curr_row) + curr_col
        
        DIRS = [[0,1],[1,0],[0,-1],[-1,0]]
        inBound = lambda i, j: 0 <= i < len(grid) and 0 <= j < len(grid[0])
        make_unique = lambda i, j: (len(grid[0]) * i) + j
        count = grids = 0
        
        # find start and end point
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:     sr, sc = i, j
                if grid[i][j] != -1:    grids += 1
        
        
        def backtrack(i, j, num):
            nonlocal count
            num |= (1 << make_unique(i, j))
            if grid[i][j] == 2:
                if bin(num).count("1") == grids:
                    count += 1
                return 
            
            for x, y in DIRS:
                new_r, new_c = i + x, j + y
                if inBound(new_r, new_c) and grid[new_r][new_c] != -1 and not bool(num & (1 << make_unique(new_r, new_c))):
                    backtrack(new_r, new_c, num)

        backtrack(sr, sc, 0)
        return count