class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:        
        validPaths = []
        def backtrack(node, curr_path):
            if node == len(graph) - 1:
                validPaths.append(curr_path.copy())
                return
            
            for neigh in graph[node]:
                curr_path.append(neigh)
                backtrack(neigh, curr_path)
                curr_path.pop()
        
        backtrack(0, [0])
        return validPaths