class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        ans = []
        
        maxHeap = [(-c, l) for l, c in freq.items()]
        
        heapq.heapify(maxHeap)
        queue = deque()
        
        while maxHeap:
            count, letter = heapq.heappop(maxHeap)
            
            ans.append(letter)
            if count < -1:  
                queue.append((count + 1, letter))
            
            if queue and queue[0][1] != ans[-1]:
                heapq.heappush(maxHeap, queue.popleft())
        
        return "".join(ans) if len(ans) == len(s) else ""
        