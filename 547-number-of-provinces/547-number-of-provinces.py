class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [i for i in range(len(isConnected))]
        ranks = [1]*len(isConnected)
        provinces = len(isConnected)
        
        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
            
        def unite(i, j):
            parentI = find(i)
            parentJ = find(j)
            nonlocal provinces
            if parentI != parentJ:
                provinces -= 1
                if ranks[parentI] >= ranks[parentJ]:
                    parent[parentJ] = parentI
                    ranks[parentI] += ranks[parentJ]
                    ranks[parentJ] = 0
                else:
                    parent[parentI] = parentJ
                    ranks[parentJ] += ranks[parentI]
                    ranks[parentI] = 0
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    unite(i, j)
                    
        return provinces