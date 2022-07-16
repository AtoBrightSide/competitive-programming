class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        isOut = lambda i,j: i < 0 or i >= m or j < 0 or j >= n 
        DIRS = [[0,1],[1,0],[0,-1],[-1,0]]
        
        memo = {}
        def dfs(i, j, moves):
            if isOut(i,j):      return 1
            
            if moves == 0:  return 0
            
            if (i, j, moves) in memo:   return memo[(i, j, moves)]
            
            count = 0
            for d in DIRS:
                x, y = d[0] + i, d[1] + j
                count += dfs(x, y, moves - 1)
                
            memo[(i, j, moves)] = count
            return memo[(i, j, moves)]
        
        return dfs(startRow, startColumn, maxMove) % ((10**9) + 7)