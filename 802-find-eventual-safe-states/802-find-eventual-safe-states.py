class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        queue = deque()
        outgoing = [0]*len(graph)
        incoming = defaultdict(list)
        for i in range(len(graph)):
            outgoing[i] = len(graph[i])
            if len(graph[i]) == 0:
                queue.append(i)
                continue
            for edge in graph[i]:
                incoming[edge].append(i)
        
        res = []
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for j in incoming[curr]:
                outgoing[j] -= 1
                if outgoing[j] == 0:
                    queue.append(j)
        res.sort()
        return res