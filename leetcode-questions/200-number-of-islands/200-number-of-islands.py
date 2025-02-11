class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRS = [[0,1],[1,0],[-1,0],[0,-1]]
        inbounds = lambda x,y: 0 <= x < len(grid) and 0 <= y < len(grid[0])
        
        parent = {}
        rank = {}
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                parent[(row, col)] = (row, col)
                rank[(row, col)] = 1 if grid[row][col] == "1" else 0
        
        def find(i, j):
            if (i, j) == parent[(i, j)]:
                return (i, j)
            
            parent[(i, j)] = find(parent[(i, j)][0], parent[(i, j)][1])
            return parent[(i, j)]
        
        def union(a, b):
            a_parent = find(a[0], a[1])
            b_parent = find(b[0], b[1])
            
            if a_parent != b_parent:
                if rank[a_parent] < rank[b_parent]:
                    parent[a_parent] = b_parent
                    rank[b_parent] += rank[a_parent]
                    rank[a_parent] = 0
                else:
                    parent[b_parent] = a_parent
                    rank[a_parent] += rank[b_parent]
                    rank[b_parent] = 0
                
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                for x, y in DIRS:
                    new_row, new_col = row + x, col + y
                    if inbounds(new_row, new_col) and grid[new_row][new_col] == "1" and grid[row][col] == "1":
                        union([row, col], [new_row, new_col])
        num = 0
        for key, val in rank.items():
            if val:     num += 1
        return num