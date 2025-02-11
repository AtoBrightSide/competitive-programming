class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dirs = [[0, 1], [1, 0]]
        
        inbounds = lambda x, y: 0 <= x < m and 0 <= y < n
        
        paths = defaultdict(int)
        
        def dfs(i, j):
            if (i, j) == (m - 1, n - 1):
                return 1
            
            if (i, j) in paths:
                return paths[(i, j)]
            
            for x, y in dirs:
                new_i, new_j = i + x, j + y
                if inbounds(new_i, new_j):
                    paths[(i, j)] += dfs(new_i, new_j)
            
            return paths[(i, j)]
        
        return dfs(0, 0)
        