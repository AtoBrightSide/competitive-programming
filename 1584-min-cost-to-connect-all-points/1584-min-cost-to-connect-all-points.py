class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        arr, res = [], 0
        
        parent = [i for i in range(len(points))]
        # rank = [1]*len(points)
        
        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return find(parent[node])
        
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i, len(points)):
                if i != j:
                    x2, y2 = points[j]
                    arr.append((abs(x2-x1) + abs(y2-y1), i, j))
        
        arr.sort()
        for mtd, i, j in arr:
            parentA = find(i)
            parentB = find(j)
            if parentA != parentB:
                res += mtd
                parent[parentB] = parentA

        
        return res