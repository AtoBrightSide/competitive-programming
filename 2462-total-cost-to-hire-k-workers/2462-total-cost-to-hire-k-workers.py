class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # put (cost, index) as tuple in min heap
        # initially heap will contain (candidates * 2) elements
        # then the next k workers will be paid.
        
        heap = []
        L = len(costs)
        used = set()
        for i, cost in enumerate(costs):
            if i < candidates or L - 1 - i < candidates:
                heappush(heap, [cost, i])
                used.add(i)
        
        total_cost = 0
        l = candidates
        r = L - l - 1
        while k:
            if heap:
                curr = heappop(heap)
                total_cost += curr[0]
            
            if l <= r < L:
                if l not in used and curr[1] <= l:
                    heappush(heap, [costs[l], l])
                    used.add(l)
                    l += 1
                elif r not in used and curr[1] >= r:
                    heappush(heap, [costs[r], r])
                    used.add(r)
                    r -= 1                
            k -= 1
        
        return total_cost