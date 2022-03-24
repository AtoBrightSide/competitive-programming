class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        count, arr = 0, []
        while True: 
            if count+1<len(heights) and heights[count+1]>heights[count]:
                if ladders > 0:
                    heapq.heappush(arr, (heights[count+1]-heights[count]))
                    ladders -= 1
                    count += 1
                elif ladders == 0 and bricks > 0:
                    temp = heapq.heappushpop(arr, heights[count+1]-heights[count])
                    if temp > bricks:
                        return count
                    else:
                        bricks -= temp
                    count = count + (1 if bricks>=0 else 0)
                    continue
            else:
                count += 1
                if count+1<len(heights) and heights[count+1]<=heights[count]:
                    continue
            if count == len(heights):
                return count-1
            if bricks<=0 and ladders<=0:
                return count
