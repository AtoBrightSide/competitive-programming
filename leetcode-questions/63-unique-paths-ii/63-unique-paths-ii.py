class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dirs = [[0, 1], [1, 0]]
        N, M = len(obstacleGrid), len(obstacleGrid[0])
        inBounds = lambda i, j : 0 <= i < N and 0 <= j < M
        
        memo = defaultdict(int)
        
        def dfs(i, j):
            if obstacleGrid[i][j] != 1:
                if (i, j) == (N-1, M-1):    return 1
                
                if (i, j) in memo:  return memo[(i, j)]
                
                for x, y in dirs:
                    new_i, new_j = i + x, j + y
                    if inBounds(new_i, new_j) and obstacleGrid[new_i][new_j] != 1:
                        memo[(i, j)] += dfs(new_i, new_j)
            
                return memo[(i, j)]
            
            return 0
        
        return dfs(0, 0)