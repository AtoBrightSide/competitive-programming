class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = [-val for key, val in freq.items()]
        heapq.heapify(maxHeap)
        queue = deque()
        time = 0
        while queue or maxHeap:
            time += 1
            if maxHeap:
                curr = heapq.heappop(maxHeap)
                if curr < -1:
                    queue.append([curr + 1, time + n])
            
            if queue and time == queue[0][1]:
                heapq.heappush(maxHeap, queue.popleft()[0])
           
        return time