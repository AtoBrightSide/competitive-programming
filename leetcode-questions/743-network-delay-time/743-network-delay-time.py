class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
        
        t = [float("inf")] * n
        t[k-1] = 0
        heap = [(0, k)]
        
        while heap:
            time, node = heappop(heap)
            for w, v in graph[node]:
                curr = time + w
                if curr < t[v-1]:
                    t[v-1] = curr
                    heappush(heap, (curr, v))
        
        minTime = max(t)
        return minTime if minTime != float("inf") else -1 