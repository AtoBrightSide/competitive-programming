class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.parent = [p for p in range(len(edges))]
        self.rank = [1 for _ in range(len(edges))]
        
        ans = []
        for u, v in edges:
            united = self.unite(u - 1, v - 1)
            if not united:
                ans = [u, v]
        
        return ans 
        
    def find(self, node):
        if self.parent[node] == node:
            return node
        
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def unite(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        
        if parent_a != parent_b:
            if self.rank[parent_a] > self.rank[parent_b]:
                self.parent[parent_b] = parent_a
                self.rank[parent_a] += self.rank[parent_b]
                self.rank[parent_b] = 0
            else:
                self.parent[parent_a] = parent_b
                self.rank[parent_b] += self.rank[parent_a]
                self.rank[parent_a] = 0
            return True
        return False