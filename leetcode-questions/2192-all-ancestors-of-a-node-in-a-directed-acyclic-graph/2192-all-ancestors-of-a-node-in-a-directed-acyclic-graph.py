class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indegrees, graph = [0] * n, defaultdict(list)
        for f, t in edges:
            graph[f].append(t)
            indegrees[t] += 1

        queue = deque()
        for i, count in enumerate(indegrees):
            if count == 0:  queue.append(i)
        
        ancestors = [set() for _ in range(n)]
        while queue:
            curr = queue.popleft()
            for node in graph[curr]:
                ancestors[node].add(curr)
                indegrees[node] -= 1
                if indegrees[node] == 0:    queue.append(node)
                for temp in ancestors[curr]:    ancestors[node].add(temp)
        
        for i in range(len(ancestors)): ancestors[i] = sorted(list(ancestors[i]))

        return ancestors