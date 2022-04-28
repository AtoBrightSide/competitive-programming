class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def checker(i, j):
            return 0<=i<len(grid) and 0<=j<len(grid[i])
        
        dirs = [[-1,0],[0,1],[1,0],[0,-1]]
        visited, best = {}, 0
        
        def dfs(i,j, area):
            if (i,j) in visited:
                return visited[(i,j)]
            if checker(i, j) and grid[i][j] == 1:
                area += 1
                print((i,j, area))
                visited[(i,j)] = area
                for x, y in dirs:
                    area = max(dfs(i+x, j+y, area), area)
            return area
                
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                best = max(dfs(i,j, 0), best)
                
        return best
    '''
    [
   0 [0,1,1],
   1 [1,0,1],
   2 [1,0,1],
   3 [0,1,1]
    ]
    '''