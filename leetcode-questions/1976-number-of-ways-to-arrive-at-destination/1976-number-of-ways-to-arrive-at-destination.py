class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((w, v))
            graph[v].append((w, u))
        
        t, ways = [float("inf")] * n, [1] * n
        heap, t[0] = [(0, 0)], 0
        
        while heap:
            time, node = heappop(heap)
            for w, v in graph[node]:
                curr = time + w
                if curr < t[v]:
                    t[v] = curr
                    heappush(heap, (curr, v))
                    ways[v] = ways[node]
                elif curr == t[v]:
                    ways[v] += ways[node]
                    
        return ways[-1] % ((10**9) + 7)