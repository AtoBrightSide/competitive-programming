class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i, edge in enumerate(edges):
            graph[edge[0]].append([succProb[i], edge[1]])
            graph[edge[1]].append([succProb[i], edge[0]])
        
        ways = [-float("inf")] * n
        heap = [[-1, start]]
        
        while heap:
            curr_prob, curr_node = heappop(heap)
            for prob, node in graph[curr_node]:
                temp = prob * -curr_prob
                if temp > ways[node]:
                    ways[node] = temp
                    heappush(heap, [-temp, node])
        
        return ways[end] if ways[end] != -float("inf") else 0.0