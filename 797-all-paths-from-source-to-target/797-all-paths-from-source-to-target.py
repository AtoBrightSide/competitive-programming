class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:        
        allPaths = []
        def traverse(node, curr):
            if node == len(graph) - 1:
                allPaths.append(curr.copy())
                return
            
            for n in graph[node]:
                curr.append(n)
                traverse(n, curr)
                curr.pop()
                
        traverse(0, [0])
        
        return allPaths