class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            x = -1*heapq.heappop(stones)
            y = -1*heapq.heappop(stones)
            if x == y:
                continue
            heapq.heappush(stones, -1*(x-y))
        return -1*stones[0] if len(stones)>0 else 0
