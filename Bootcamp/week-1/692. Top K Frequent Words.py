class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        res,r = [],[]
        for key, v in freq.items():
            heapq.heappush(res, (-v,key))
        for i in range(k):
            val=heapq.heappop(res)
            r.append(val[1])
        return r
