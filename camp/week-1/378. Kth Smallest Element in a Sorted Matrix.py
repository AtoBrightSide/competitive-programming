class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        for l in matrix:
            arr += l
        
        heapq.heapify(arr)
        for i in range(k):
            if i == k-1:
                return arr[0]
            heapq.heappop(arr)
