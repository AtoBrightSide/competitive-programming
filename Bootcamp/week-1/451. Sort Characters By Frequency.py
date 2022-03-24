class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        
        heap=[]
        for key, val in freq.items():
            heap.append((val, key))
        res = ""
        heapq.heapify(heap)
        while heap:
            temp = heapq.heappop(heap)
            res = temp[0]*temp[1] + res
        return(res)