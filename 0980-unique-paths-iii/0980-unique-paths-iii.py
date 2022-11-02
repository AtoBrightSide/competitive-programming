class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        DIRS = [[0,1],[1,0],[0,-1],[-1,0]]
        inBound = lambda i, j: 0 <= i < len(grid) and 0 <= j < len(grid[0])
        count = grids = 0
        
        # find start and end point
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:     sr, sc = i, j
                if grid[i][j] != -1:    grids += 1
        
        def backtrack(i, j, so_far):
            nonlocal count
            if grid[i][j] == 2:
                if len(so_far) == grids:
                    count += 1
                return 
            
            for x, y in DIRS:
                new_r, new_c = i +  x, j + y
                if inBound(new_r, new_c) and grid[new_r][new_c] != -1 and (new_r, new_c) not in so_far:
                    so_far.add((new_r, new_c))
                    backtrack(new_r, new_c, so_far)
                    so_far.remove((new_r, new_c))
        
        backtrack(sr, sc, set([(sr, sc)]))
        return count