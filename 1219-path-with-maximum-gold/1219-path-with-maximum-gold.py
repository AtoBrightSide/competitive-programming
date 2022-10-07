class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        dirs = [[0,1], [0,-1],[1,0],[-1,0]]
        inBounds = lambda i, j: 0 <= i < len(grid) and 0 <= j < len(grid[0])
        vis = set()
        
        def traverse(row, col):
            gold = grid[row][col]
            vis.add((row, col))
            
            for x, y in dirs:
                i, j = row + x, col + y
                if inBounds(i, j) and (i,j) not in vis and grid[i][j] != 0:
                    gold = max(gold, grid[row][col] + traverse(i, j))
            
            vis.remove((row, col))
            return gold
        
        maxGold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0: 
                    maxGold = max(maxGold, traverse(i, j))
        
        return maxGold