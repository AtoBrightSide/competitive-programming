class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        DIRS = [[0,1], [1,0], [0,-1], [-1,0]]
        isValid = lambda i,j: 0 <= i < m and  0 <= j < n
        
        grid = [[0 for i in range(n)] for j in range(m)]
        
        guarded = set()
        for i in range(max(len(guards), len(walls))):
            if i < len(guards):
                row, col = guards[i]
                grid[row][col] = "G"
                guarded.add((row, col))
            if i < len(walls):
                row, col = walls[i]
                grid[row][col] = "W"
                guarded.add((row, col))
        
        def simulate(i, j):
            for d in DIRS:
                x, y = d[0] + i, d[1] + j
                while isValid(x,y) and grid[x][y] != "W" and grid[x][y] != "G":
                    guarded.add((x,y))
                    x += d[0]
                    y += d[1]
        
        for r, c in guards:
            simulate(r, c)
                    
        return m*n - len(guarded)