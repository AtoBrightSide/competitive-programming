class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        isValid = lambda i,j: 0 <= i < len(grid) and 0 <= j < len(grid[0])
        DIRS = [[0,1],[0,-1],[1,0],[-1,0]]
        rank, parent = {}, {}
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rank[(i,j)] = 0 if grid[i][j] == 0 else 1
                parent[(i,j)] = (i,j)
        
        def find(i,j):
            if (i, j) == parent[(i,j)]:
                return i,j
            
            i,j = find(parent[(i, j)][0], parent[(i, j)][1])
            return i, j
        
        def unite(i1, j1, i2, j2):
            p1 = find(i1, j1)
            p2 = find(i2, j2)
            
            if p1 != p2:
                if rank[p1] >= rank[p2]:
                    parent[p2] = p1
                    rank[p1] += rank[p2]
                    rank[p2] = 0
                else:
                    parent[p1] = p2
                    rank[p2] += rank[p1]
                    rank[p1] = 0
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for d in DIRS:
                    x, y = d[0] + i, d[1] + j
                    if grid[i][j] == 1 and isValid(x,y) and grid[x][y] == 1:    unite(i, j, x, y)
        
        ans = max(rank.values())
        
        return ans