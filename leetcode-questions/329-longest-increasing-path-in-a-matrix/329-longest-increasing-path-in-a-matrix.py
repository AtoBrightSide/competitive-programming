class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        def inBounds(i, j):
            return 0 <= i < len(matrix) and 0 <= j < len(matrix[i])
        
        from_here = {}
        @lru_cache(None)
        def dfs(i, j, count):
            best = 0
            for x, y in dirs:
                x_i, y_j = x+i, y+j
                if inBounds(x_i, y_j) and matrix[x_i][y_j] > matrix[i][j]:
                    best = max(best, count + dfs(x_i, y_j, count))
            
            return max(count, best)
            
            
        maxPath = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                maxPath = max(maxPath, dfs(i, j, 1))
                
        return maxPath