class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        def inBounds(i, j):
            return 0 <= i < len(matrix) and 0 <= j < len(matrix[i])
        
        from_here = {}
        def dfs(i, j, count):
            if (i, j) in from_here:
                return from_here[(i, j)]
            best = 0
            for x, y in dirs:
                x_i, y_j = x+i, y+j
                if inBounds(x_i, y_j) and matrix[x_i][y_j] > matrix[i][j]:
                    best = max(best, count + dfs(x_i, y_j, count))
            from_here[(i, j)] = max(count, best)
            
            return from_here[(i, j)]
            
        maxPath = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (i, j) in from_here:
                    maxPath = max(maxPath, from_here[(i, j)])
                else:
                    maxPath = max(maxPath, dfs(i, j, 1))
                
        return maxPath