class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dirs = [[1, 1], [1, -1],  [-1, -1], [-1, 1], [0, 1], [1, 0], [-1, 0], [0, -1]]
        n = len(grid)
        
        def inBounds(i, j):
            return 0 <= i < n and 0 <= j < n
        
        if grid[0][0] != 0:
            return -1
        
        queue, visited = deque(), set()
        
        queue.append([1, 0, 0])
        visited.add((0,0))
        
        while queue:
            path, i, j = queue.popleft()
            if (i, j) == (n - 1, n - 1):
                return path
            
            for x, y in dirs:
                if inBounds(i+x, j+y) and grid[i+x][j+y] == 0 and (i+x, j+y) not in visited:
                    visited.add((i+x, j+y))
                    queue.append([path+1, i+x, j+y])
        
        return -1