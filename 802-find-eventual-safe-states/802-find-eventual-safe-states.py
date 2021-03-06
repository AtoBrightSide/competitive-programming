class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # denoting 0 for untouched, 1 for processing and 2 for safe        
        n = len(graph)
        colors = [0] * n
        
        def dfs(cur):
            if colors[cur] == 2:
                return True
            
            if colors[cur] == 1:
                return False
            
            colors[cur] = 1
            isSafe = True
            
            for i in graph[cur]: 
                isSafe = isSafe and dfs(i)
            
            colors[cur] = 2 if isSafe else 0
            return isSafe
        res = []
        for i in range(n):
            if colors[i] == 0:
                dfs(i)
            if colors[i] == 2:
                res.append(i)
        
        
        return res
        