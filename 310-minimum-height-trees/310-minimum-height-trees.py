from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        edge_count = [0] * n
        
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
            edge_count[a] += 1
            edge_count[b] += 1
        
        leaves_queue = deque()
        for node, edge in enumerate(edge_count):
            if edge == 1:
                leaves_queue.append(node)
        
        while leaves_queue:
            if len(graph) <= 2:
                break
            for k in range(len(leaves_queue)):
                cur = leaves_queue.popleft()
                parent = graph[cur].pop()
                graph.pop(cur)
                graph[parent].remove(cur)
                edge_count[parent] -= 1

                if edge_count[parent] == 1:
                    leaves_queue.append(parent)
            
        return graph.keys() if graph else [0]