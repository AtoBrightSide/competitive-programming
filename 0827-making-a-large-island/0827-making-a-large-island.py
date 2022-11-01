class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        inBounds = lambda i, j: 0 <= i < len(grid) and 0 <= j < len(grid)
        
        rank = {(i, j): (1 if grid[i][j] == 1 else 0) for j in range(len(grid)) for i in range(len(grid))}
        parent = {(i, j): (i, j) for j in range(len(grid)) for i in range(len(grid))}
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1:
                    for x, y in DIRS:
                        new_i, new_j = i + x, j + y
                        if inBounds(new_i, new_j) and grid[new_i][new_j] == 1:
                            self.unite((i, j), (new_i, new_j), rank, parent)
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                self.find((i, j), rank, parent)
        
        largest = rank[parent[(0, 0)]] - 1
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 0:
                    used = set()
                    curr_island = 0
                    for x, y in DIRS:
                        new_i, new_j = i + x, j + y
                        if inBounds(new_i, new_j) and parent[(new_i, new_j)] not in used:
                            curr_island += rank[parent[(new_i, new_j)]]
                            used.add(parent[(new_i, new_j)])
                    largest = max(largest, curr_island)
        
        return largest + 1
                    
        
    def find(self, node, rank, parent):
        if node == parent[node]:
            return node
        
        parent[node] = self.find(parent[node], rank, parent)
        return parent[node]
    
    def unite(self, a, b, rank, parent):
        pa = self.find(a, rank, parent)
        pb = self.find(b, rank, parent)
        
        if pa != pb:
            if rank[pa] >= rank[pb]:
                parent[pb] = pa
                rank[pa] += rank[pb]
                rank[pb] = 0
            else:
                parent[pa] = pb
                rank[pb] += rank[pa]
                rank[pa] = 0
        