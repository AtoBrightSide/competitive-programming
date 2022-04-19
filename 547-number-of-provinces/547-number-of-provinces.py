class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [i for i in range(len(isConnected))]
        provinces = len(isConnected)
        def unite(i, j):
            nonlocal provinces
            parent_of_a = find(i)
            parent_of_b = find(j)
            
            if parent_of_a == parent_of_b:
                return
            
            parent[parent_of_b] = parent_of_a
            provinces -= 1
            
        def find(i):
            if parent[i] == i:
                return i
            return find(parent[i])
            

        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    unite(i, j)
    
        return provinces