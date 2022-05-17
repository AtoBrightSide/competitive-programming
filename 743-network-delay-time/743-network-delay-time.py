class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        travels = defaultdict(list)
        for src, target, time in times:
            travels[src].append((time, target))
        
        heap = [(0, k)]
        sent = set()
        maxt = 0
        
        while heap:
            time, node = heapq.heappop(heap)
            if node not in sent:
                sent.add(node)
                maxt = max(maxt, time)
                
                for t, nd in travels[node]:
                    if nd not in sent:
                        heapq.heappush(heap, (t + time, nd))
            
        print(sent)
        return maxt if len(sent) == n else -1
