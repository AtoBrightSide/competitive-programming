class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # 1 is blue and 0 is blue
        graph = defaultdict(list)
        for src, dst in redEdges:   
            graph[(src, 0)].append(dst)
        for src, dst in blueEdges:  
            graph[(src, 1)].append(dst)
        
        shortest = [float('inf')] * n
        shortest[0] = 0
        queue = deque([curr for curr in graph.keys() if curr == (0, 1) or curr == (0, 0)])
        move = 1
        vis = set()
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                vis.add(curr)
                src, color = curr
                for dst in graph[curr]:
                    shortest[dst] = min(move, shortest[dst])
                    if (dst, 1 - color) in graph and (dst, 1 - color) not in vis:
                        queue.append((dst, 1 - color))        
            move += 1
            
        for i, val in enumerate(shortest):
            if val == float("inf"): shortest[i] = -1
                
        return shortest