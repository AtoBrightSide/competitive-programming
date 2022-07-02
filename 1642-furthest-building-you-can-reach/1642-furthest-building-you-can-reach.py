class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        
        for i in range(len(heights) - 1):
            curr = heights[i+1] - heights[i]
            if curr > 0:
                if ladders > 0:
                    ladders -= 1
                    heappush(heap, curr)
                else:
                    temp = heappushpop(heap, curr)
                    bricks -= temp
                if bricks < 0:  return i
                        
        return len(heights) - 1